# Phase 1: Foundation Setup

## Objective
Create working SQLite database from iMax column usage data that can be queried to assist with SQL generation.

## Phase 1 Complete ✅

**Database stats:**
- 4 tables loaded
- 1,961 columns indexed
- All pulled_date: 2026-02-12

---

# Phase 2: AI Query Access

## Objective
Enable AI assistant to query schema database directly without copy-paste.

## Phase 2 Complete ✅

**Access method:** Pylance `mcp_s_pylanceRunCodeSnippet` executes Python → queries SQLite

---

# Phase 3: Web UI

## Objective
Human-browsable interface for exploring schema documentation.

## Phase 3 Complete ✅

**Features:** Table browser, global search, quality filters, joins tab, glossary tab.

---

# Phase 4: Data Expansion (Salesforce)

## Objective
Add Salesforce schemas and reference data (ID prefixes, FK detection).

## Phase 4 Complete ✅

- [x] sfdcpsa — 46 tables (Salesforce PSA)
- [x] sfdcapttus — 62 tables (Salesforce Apttus)
- [x] sfdcccrm — 102 tables (Salesforce CCRM)
- [x] sfdcsmax — 143 tables (Salesforce SMax)
- [x] ID prefix decoder from `temp_ids.csv` — 37 prefixes
- [x] Auto-detected FK relationships from `temp_columns.csv` — 609 links
- [x] New web UI tabs: "Detected FKs" and "ID Prefixes"
- [x] Multi-schema notebook (`schema_analyzer.ipynb`) with `SCHEMAS` list config
- [x] iMax CSVs organized into `imports/column-usage/imax/` subfolder
- [x] Temp files moved to `imports/temp/`

---

# Phase 5: SAP/ERP Tables

## Objective
Add ERP schemas to complete enterprise coverage.

## Phase 5 Complete ✅

- [x] mcp — 626 tables (ERP)
- [x] mp1 — 874 tables (ERP)
- [x] wpp — 1,140 tables (SAP/ERP)
- [x] Sampling support for large tables (`MAX_ROWS_FULL_SCAN=50M`, `SAMPLE_SIZE=10M`)
- [x] Resume mode (`SKIP_EXISTING = True`) for interrupted runs
- [x] `SKIP_TABLES` config for monster tables (acdoca, bseg)
- [x] Pure SQL queries generated for acdoca (384 cols) and bseg (385 cols) using `TABLESAMPLE (10 PERCENT)`
- [x] GitHub Pages deployment — `data.json` copied to root (build/ is gitignored)
- [x] Live at https://sirhcrd.github.io/schema-intel/

## Grand Totals

| Metric | Count |
|--------|-------|
| Schemas | 8 |
| Tables | 1,772 |
| Columns | 75,946 |
| FK Links (auto-detected) | 609 |
| ID Prefixes | 37 |
| Manual Joins | 19 |
| Web UI Tabs | 5 (Tables, Joins, Detected FKs, ID Prefixes, Glossary) |

---

# Phase 6: Future Enhancements (Planned)

## Potential Work
- [ ] Import acdoca and bseg CSVs (SQL warehouse queries ready, need execution)
- [ ] Glossary content — add business term definitions
- [ ] Column descriptions — human-written explanations for key columns
- [ ] Data lineage — document ETL flows between schemas
- [ ] Schema diff — detect changes between analysis runs
- [ ] Additional schemas as needed
