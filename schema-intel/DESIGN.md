# Design Overview

## High-Level Flow

```
[CSV Exports]  →  [csv_to_markdown.py]  →  [data/tables/*.md]
                                                    ↓
[Manual edits]  →  [data/joins.md, glossary.md]  ←──┤
                                                    ↓
[temp_ids.csv] → [build_references.py] → [data/id-prefixes.md]
[temp_columns.csv] →                   → [data/detected-joins.md]
                                                    ↓
                                          [build_db.py]
                                                    ↓
                           ┌────────────────────────┴────────────────────────┐
                           ↓                                                 ↓
                    [build/schema.db]                              [build/data.json]
                           ↓                                                 ↓
               [AI queries via MCP/copy-paste]                    [index.html Web UI]
```

## Key Architectural Decisions

### Decision: Markdown as Source of Truth
- **Chosen approach:** All schema metadata lives in Markdown files with YAML frontmatter
- **Alternatives considered:** 
  - Direct SQLite editing (harder to review changes, no good diff)
  - JSON files (less human-readable, harder to add prose descriptions)
  - YAML-only (verbose for large column lists)
- **Reasoning:** Markdown is human-readable, version-controllable, and allows mixing structured data (tables) with prose (notes, descriptions)
- **Trade-offs accepted:** Need build step to generate queryable outputs

### Decision: One File Per Table
- **Chosen approach:** Each table gets its own `data/tables/{table_name}.md` file
- **Alternatives considered:** 
  - Single large file (unwieldy at scale)
  - Grouped by source system (harder to find specific tables)
- **Reasoning:** Scales with tooling; individual tables can be updated independently; clean git history
- **Trade-offs accepted:** Many small files (handled by tooling, not manual navigation)

### Decision: SQLite for AI Access
- **Chosen approach:** Build script generates `schema.db` that can be queried
- **Alternatives considered:**
  - PostgreSQL (overkill for read-only metadata)
  - JSON search (slower, less expressive queries)
- **Reasoning:** Zero-setup, portable, excellent tooling support, can be queried via MCP or copy-paste
- **Trade-offs accepted:** Must rebuild after Markdown changes

### Decision: Static Web UI
- **Chosen approach:** Single HTML file reading from `data.json` served via GitHub Pages
- **Alternatives considered:**
  - Server-rendered app (unnecessary complexity for read-only data)
  - Multiple HTML pages (harder to maintain)
- **Reasoning:** No backend needed; works anywhere; can be shared via URL
- **Trade-offs accepted:** Must rebuild JSON when data changes; `data.json` must be copied to project root since `build/` is gitignored — `build_json.py` handles this automatically via `shutil.copy2`
- **Deployment:** GitHub Pages at `https://sirhcrd.github.io/schema-intel/`

### Decision: Auto-Detect FK via ID Prefix
- **Chosen approach:** Parse sample column values, extract Salesforce ID prefixes, match to tables
- **Alternatives considered:**
  - Manual FK documentation (doesn't scale to 600+ relationships)
  - Query system metadata (not available in Databricks/read-only)
- **Reasoning:** Salesforce IDs have 3-char prefixes that identify object type; sample data reveals which columns link where
- **Trade-offs accepted:** Some false positives when prefixes collide; must verify before critical use

### Decision: Sampling for Large Tables
- **Chosen approach:** Tables exceeding `MAX_ROWS_FULL_SCAN` (50M rows) are sampled using `df.sample(False, fraction)` in the notebook, with `SAMPLE_SIZE` (10M rows) as the target
- **Alternatives considered:**
  - Full scan always (impractical for 1B+ row tables — hours per table)
  - Skip large tables entirely (loses coverage)
- **Reasoning:** Column usage percentages are statistically equivalent at 10M rows vs. full scan for tables with billions of rows; sampling completes in minutes vs. hours
- **Trade-offs accepted:** Usage % is approximate (±1-2%) for sampled tables; frontmatter notes when sampling was used

### Decision: SQL Warehouse Queries for Monster Tables
- **Chosen approach:** For tables too large even with notebook sampling (e.g., `acdoca` with 1.3B rows, `bseg`), generate pure SQL queries using `TABLESAMPLE (10 PERCENT)` and run them directly on a SQL warehouse
- **Alternatives considered:**
  - Running in notebook with aggressive sampling (still too slow due to Spark overhead)
  - Skipping entirely (leaves critical SAP tables undocumented)
- **Reasoning:** SQL warehouse bypasses Spark session overhead; `TABLESAMPLE` pushes sampling to the storage layer
- **Trade-offs accepted:** Requires manual execution + CSV export; results must be placed in correct import folder

### Decision: Resume Mode (SKIP_EXISTING)
- **Chosen approach:** Notebook checks if output CSV already exists for each table and skips it when `SKIP_EXISTING = True`
- **Alternatives considered:**
  - Always re-analyze (wastes time on schemas with 1000+ tables when runs are interrupted)
  - Checkpoint files (more complex for same benefit)
- **Reasoning:** Simple, stateless — just checks filesystem. Allows interrupted runs to resume without re-doing work
- **Trade-offs accepted:** Must manually delete a CSV to force re-analysis of that table

## Data Model

### Table Metadata (Markdown frontmatter)
```yaml
---
table: imax_case           # Canonical table name
source: imax               # Source system (imax, salesforce, sap, erp)
pulled_date: 2026-02-12    # When column stats were gathered
row_count: 2400000         # Approximate row count (optional)
---
```

### Column Data (Markdown table)
| Field | Type | Description |
|-------|------|-------------|
| Column | string | Column name |
| Type | string | Data type (string, int, datetime, etc.) |
| Usage % | float | Percentage of rows with non-null values |
| Quality | enum | trusted (>50% usage), neutral, dead (<5% usage) |
| Description | string | Human-written explanation (optional) |

### Join Definitions (`data/joins.md`)
```markdown
## imax_case → zone_mapping
- **Join column:** service_zone
- **Type:** LEFT JOIN (not all cases have zone)
- **Cardinality:** many-to-one
- **Notes:** Zone mapping is reference data, rarely changes
```

### SQLite Schema
```sql
CREATE TABLE tables (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    source TEXT,
    description TEXT,
    row_count INTEGER,
    pulled_date TEXT
);

CREATE TABLE columns (
    id INTEGER PRIMARY KEY,
    table_id INTEGER REFERENCES tables(id),
    name TEXT NOT NULL,
    data_type TEXT,
    usage_pct REAL,
    quality TEXT,  -- 'trusted', 'neutral', 'dead'
    description TEXT,
    UNIQUE(table_id, name)
);

CREATE TABLE joins (
    id INTEGER PRIMARY KEY,
    from_table TEXT,
    from_column TEXT,
    to_table TEXT,
    to_column TEXT,
    join_type TEXT,
    cardinality TEXT,
    notes TEXT
);

CREATE TABLE detected_joins (
    id INTEGER PRIMARY KEY,
    from_table TEXT,
    from_column TEXT,
    to_table TEXT,
    to_column TEXT DEFAULT 'id',
    prefix TEXT,           -- SF ID prefix that matched
    confidence TEXT        -- 'auto-detected'
);

CREATE TABLE id_prefixes (
    prefix TEXT PRIMARY KEY,
    tables TEXT,           -- comma-separated table names
    description TEXT
);
```

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| Stale column stats | Check `pulled_date` in frontmatter | Re-run analysis notebook, regenerate |
| Missing table | Query returns no results | Add table via CSV import or manual creation |
| Broken join path | Query plans fail | Check `data/joins.md`, update relationships |
| Build script error | Non-zero exit code | Fix Markdown syntax, rebuild |

## What Would Force a Redesign

- Need for real-time schema sync → would require live DB connection
- Multi-user concurrent editing → would need proper backend
- Tables exceed 10,000+ → may need pagination or lazy loading in web UI
- Non-Philips deployment → may need auth/access controls

> **Note:** The system scaled past the original 1,000-table threshold without
> redesign. At 1,772 tables / 75,946 columns, the static architecture still
> performs well thanks to client-side search and JSON compression.
