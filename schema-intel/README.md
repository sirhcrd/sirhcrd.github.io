# Schema Intelligence System

## Purpose
A queryable knowledge base of your company's database landscape that enables accurate SQL generation by AI assistants and provides human-readable documentation for learning and sharing.

## Non-Goals
- Real-time sync with production databases
- Query execution engine (this documents structure, not data)
- Replacing your coworker's existing tools — this extends them

## Core Constraints
- **Data volume:** Hundreds of tables, thousands of columns (scales via tooling)
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

1. Set `CATALOG` and `SCHEMA` in cell 2 (e.g., `prod_l1`, `sfdcpsa`)
2. Run all cells — auto-discovers all tables
3. Download ZIP from workspace folder

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
│
├── data/                  # Markdown source files (source of truth)
│   ├── tables/            # One .md per table (49 tables)
│   ├── joins.md           # Manual relationship definitions
│   ├── detected-joins.md  # Auto-detected FK relationships
│   ├── glossary.md        # Business terms → technical mapping
│   └── id-prefixes.md     # Salesforce ID decoder (37 prefixes)
│
├── imports/               # Raw data to process
│   └── column-usage/      # CSV exports organized by schema
│       ├── sfdcpsa/       # Salesforce PSA tables
│       ├── temp_ids.csv   # ID samples for prefix decoder
│       └── temp_columns.csv # Column samples for FK detection
│
├── build/                 # Generated outputs
│   ├── schema.db          # SQLite database
│   └── data.json          # For web UI
│
├── scripts/               # Build tooling
│   ├── batch_build.py     # One-command full rebuild
│   ├── csv_to_markdown.py # CSV → Markdown table files
│   ├── build_db.py        # Markdown → SQLite
│   ├── build_json.py      # Markdown → JSON
│   └── build_references.py # ID prefixes + FK detection
│
└── index.html             # Web UI
```

## Data Sources

| Source | Status | What it provides |
|--------|--------|------------------|
| iMax tables | ✅ Imported | 4 tables, ~1,961 columns |
| sfdcpsa tables | ✅ Imported | 45 tables (PSA/Salesforce) |
| `temp_ids` | ✅ Processed | 37 ID prefixes decoded |
| `temp_columns` | ✅ Processed | 609 FK relationships detected |
| SAP/ERP tables | 🔄 Future | Additional coverage |

## Git Workflow
- **Branches:** `feature/description`, `fix/description`
- **Commits:** `feat(tables): add pse_milestone_c metadata`
