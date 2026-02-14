# Schema Intelligence System

## Purpose
A queryable knowledge base of your company's database landscape that enables accurate SQL generation by AI assistants and provides human-readable documentation for learning and sharing.

## Non-Goals
- Real-time sync with production databases
- Query execution engine (this documents structure, not data)
- Replacing your coworker's existing tools — this extends them

## Live Site
**GitHub Pages:** [https://sirhcrd.github.io/schema-intel/](https://sirhcrd.github.io/schema-intel/)

## Core Constraints
- **Data volume:** 1,772 tables, 75,946 columns across 8 schemas
- **Source of truth:** Markdown files in `data/` directory
- **Consistency model:** Manual updates via notebook runs + exports
- **Deployment:** GitHub Pages for web UI, local SQLite for AI access

## Success Criteria
- [x] AI assistant can query column metadata and write accurate SQL
- [x] Web UI is browsable and searchable by humans
- [x] Join paths between tables are documented and queryable
- [x] Column quality indicators help identify reliable vs. junk columns
- [x] Salesforce ID prefixes decoded for FK navigation

## Invariants
- Markdown files are always the source of truth
- Build outputs (SQLite, JSON) are derived, never edited directly
- Every table file includes `pulled_date` for freshness tracking

## Primary Risks
- Coverage gaps: tables not yet analyzed will have no column metadata
- Stale data: column usage stats reflect point-in-time analysis

---

## Quick Start Commands

**Full rebuild (after adding new CSVs):**
```bash
python3 scripts/batch_build.py
```

**Build ID prefixes and FK detection (after updating temp_ids/temp_columns):**
```bash
python3 scripts/build_references.py
python3 scripts/build_json.py  # regenerate JSON
```

**Individual steps:**
```bash
python3 scripts/csv_to_markdown.py   # CSV → Markdown
python3 scripts/build_db.py          # Markdown → SQLite
python3 scripts/build_json.py        # Markdown → JSON
```

**View web UI:**
```bash
python3 -m http.server 8080
# Open http://localhost:8080
```

---

## Adding New Tables

### Step 1: Run Column Analysis (Databricks)

Use the schema analyzer notebook: `databaseColumnAnalysis/schema_analyzer.ipynb`

1. Set `SCHEMAS` list in cell 2 (e.g., `["sfdcpsa", "sfdcapttus"]`)
2. Optionally configure:
   - `SKIP_TABLES` — list of tables to skip (e.g., monster tables like `acdoca`)
   - `SKIP_EXISTING = True` — resume mode, skips tables that already have output CSVs
   - `MAX_ROWS_FULL_SCAN = 50_000_000` — tables above this get sampled
   - `SAMPLE_SIZE = 10_000_000` — sample size for large tables
3. Run all cells — auto-discovers all tables in each schema
4. Download ZIP from workspace folder

> **Monster tables (e.g., acdoca, bseg):** For tables with 1B+ rows that are too slow
> even with sampling, use the pure SQL queries generated during Phase 5 and run them
> directly on a SQL warehouse.

### Step 2: Import to Schema Intel

```bash
# Unzip CSVs into a schema subfolder
mkdir -p imports/column-usage/your_schema/
unzip ~/Downloads/your_schema_column_analysis.zip -d imports/column-usage/your_schema/

# Rebuild everything
python3 scripts/batch_build.py
```

### Step 3: Verify

- Check web UI for new tables
- Test AI queries against new columns

## Project Structure
```
schema-intel/
├── README.md              # This file
├── DESIGN.md              # Architecture decisions
├── TASK.md                # Current work in progress
├── data.json              # Root copy for GitHub Pages (build/ is gitignored)
│
├── data/                  # Markdown source files (source of truth)
│   ├── tables/            # One .md per table (1,772 tables)
│   ├── joins.md           # Manual relationship definitions (19 joins)
│   ├── detected-joins.md  # Auto-detected FK relationships (609 links)
│   ├── glossary.md        # Business terms → technical mapping
│   └── id-prefixes.md     # Salesforce ID decoder (37 prefixes)
│
├── imports/               # Raw data to process
│   ├── column-usage/      # CSV exports organized by schema
│   │   ├── imax/          # 4 tables
│   │   ├── sfdcpsa/       # 46 tables (Salesforce PSA)
│   │   ├── sfdcapttus/    # 62 tables (Salesforce Apttus)
│   │   ├── sfdcccrm/      # 102 tables (Salesforce CCRM)
│   │   ├── sfdcsmax/      # 143 tables (Salesforce SMax)
│   │   ├── mcp/           # 626 tables (ERP)
│   │   ├── mp1/           # 874 tables (ERP)
│   │   └── wpp/           # 1,140 tables (ERP/SAP)
│   └── temp/              # Temp files for reference building
│       ├── temp_ids.csv   # ID samples for prefix decoder
│       └── temp_columns.csv # Column samples for FK detection
│
├── build/                 # Generated outputs (gitignored)
│   ├── schema.db          # SQLite database
│   └── data.json          # For web UI
│
├── scripts/               # Build tooling
│   ├── batch_build.py     # One-command full rebuild
│   ├── csv_to_markdown.py # CSV → Markdown table files
│   ├── build_db.py        # Markdown → SQLite
│   ├── build_json.py      # Markdown → JSON (outputs to build/ + root)
│   └── build_references.py # ID prefixes + FK detection
│
└── index.html             # Web UI (5 tabs)
```

## Data Sources

| Source | Schema | Status | Tables | Columns |
|--------|--------|--------|--------|---------|
| iMax | imax | ✅ Imported | 4 | ~1,961 |
| Salesforce PSA | sfdcpsa | ✅ Imported | 46 | — |
| Salesforce Apttus | sfdcapttus | ✅ Imported | 62 | — |
| Salesforce CCRM | sfdcccrm | ✅ Imported | 102 | — |
| Salesforce SMax | sfdcsmax | ✅ Imported | 143 | — |
| ERP (MCP) | mcp | ✅ Imported | 626 | — |
| ERP (MP1) | mp1 | ✅ Imported | 874 | — |
| SAP/ERP (WPP) | wpp | ✅ Imported | 1,140 | — |
| **Totals** | | | **1,772** | **75,946** |

**Reference data:**
- `temp_ids` → 37 Salesforce ID prefixes decoded
- `temp_columns` → 609 FK relationships auto-detected

## Git Workflow
- **Branches:** `feature/description`, `fix/description`
- **Commits:** `feat(tables): add pse_milestone_c metadata`
