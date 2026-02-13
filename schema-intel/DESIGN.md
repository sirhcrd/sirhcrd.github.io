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
- **Chosen approach:** Single HTML file reading from `build/data.json` on GitHub Pages
- **Alternatives considered:**
  - Server-rendered app (unnecessary complexity for read-only data)
  - Multiple HTML pages (harder to maintain)
- **Reasoning:** No backend needed; works anywhere; can be shared via URL
- **Trade-offs accepted:** Must rebuild JSON when data changes

### Decision: Auto-Detect FK via ID Prefix
- **Chosen approach:** Parse sample column values, extract Salesforce ID prefixes, match to tables
- **Alternatives considered:**
  - Manual FK documentation (doesn't scale to 600+ relationships)
  - Query system metadata (not available in Databricks/read-only)
- **Reasoning:** Salesforce IDs have 3-char prefixes that identify object type; sample data reveals which columns link where
- **Trade-offs accepted:** Some false positives when prefixes collide; must verify before critical use

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
- Tables exceed 1000+ → may need sharding or categorization
- Non-Philips deployment → may need auth/access controls
