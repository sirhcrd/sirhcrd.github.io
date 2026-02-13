# Phase 1: Foundation Setup

## Objective
Create working SQLite database from iMax column usage data that can be queried to assist with SQL generation.

## Context
Four iMax tables have been analyzed via the column usage notebook. We need to convert these CSVs into the Markdown-first format and build the SQLite database.

## Files in Scope
- `imports/column-usage/*.csv` — source data
- `data/tables/*.md` — generated table docs
- `data/joins.md` — join definitions (extract from existing guide)
- `scripts/csv_to_markdown.py` — conversion script
- `scripts/build_db.py` — SQLite generator
- `build/schema.db` — output database

## Out of Scope
- Web UI (Phase 3)
- MCP server integration (Phase 2)
- PSA/CCRM/SAP tables (future data gathering)
- ID prefix decoder (waiting on coworker export)

## Constraints
- All generated Markdown must include `pulled_date` in frontmatter
- Quality flags: trusted (≥50% usage), neutral (5-50%), dead (<5%)
- Column names must be preserved exactly as they appear in source

## Agent Boundaries (for this task)

✅ **Always do:**
- Preserve original column names from CSVs
- Include `pulled_date` in all generated files
- Validate SQLite build completes without errors

⚠️ **Ask first:**
- Changing quality threshold percentages
- Adding columns not in source CSVs
- Modifying the SQLite schema

🚫 **Never do:**
- Delete source CSV files
- Modify the column usage notebook
- Commit build/ outputs (gitignored)

## Definition of Done
- [x] Folder structure created
- [x] README.md, DESIGN.md, TASK.md created
- [x] iMax CSVs copied to `imports/column-usage/`
- [x] `csv_to_markdown.py` converts CSVs to table Markdown files
- [x] Join data extracted from `database_reference_guide.html` into `data/joins.md`
- [x] `build_db.py` generates `schema.db` from Markdown
- [x] Test query returns accurate column data

## Phase 1 Complete

**Database stats:**
- 4 tables loaded
- 1,961 columns indexed
- All pulled_date: 2026-02-12

**Sample query — "which serial number columns are reliable?"**
```sql
SELECT t.name, c.name, c.usage_pct, c.quality 
FROM columns c JOIN tables t ON c.table_id = t.id 
WHERE c.name LIKE '%serial%' ORDER BY c.usage_pct DESC;
```
→ Returns 22 columns, 7 trusted (>50%), 8 neutral, 7 dead

---

# Phase 2: AI Query Access

## Objective
Enable AI assistant to query schema database directly without copy-paste.

## Solution
- MCP SQLite server configured in `.vscode/mcp.json`
- AI queries via Pylance Python code snippet execution
- Direct SQLite access to `build/schema.db`

## Definition of Done
- [x] MCP server config created (`.vscode/mcp.json`)
- [x] Server running in VS Code
- [x] AI can query tables, columns, usage stats
- [x] Test query returns accurate results

## Phase 2 Complete

**Access method:** Pylance `mcp_s_pylanceRunCodeSnippet` executes Python → queries SQLite

**Example query in action:**
```
User: "What serial number columns are reliable?"
AI: [queries schema.db] → Returns 7 trusted columns with >50% usage
```

---

# Phase 3: Web UI

## Objective
Human-browsable interface for exploring schema documentation.

## Scope
- Static HTML reading from `build/data.json`
- Table browser with column quality indicators
- Global search across all tables/columns
- Join path visualization
- Glossary tab

## Definition of Done
- [x] `build_json.py` generates JSON from Markdown
- [x] `index.html` web UI created
- [x] Table cards with expandable column lists
- [x] Quality filter buttons (All/Trusted/Neutral/Dead)
- [x] Global search with column/table results
- [x] Joins tab with relationship visualization
- [x] Glossary tab with term mapping
- [x] Keyboard shortcuts (/ to search, Esc to close)

## Phase 3 Complete

**To view:**
```bash
cd schema-intel && python3 -m http.server 8080
# Open http://localhost:8080
```

**Features:**
- Dark theme matching existing database guide
- Expandable table cards with quality indicators
- Real-time search across 1,961 columns
- Filter columns by quality (trusted/neutral/dead)
- Join path documentation
- Business term glossary

---

# Phase 4: Data Expansion

## Objective
Add more tables and reference data.

## Completed
- [x] PSA/Salesforce tables (`prod_l1.sfdcpsa`) — 45 tables added
- [x] ID prefix decoder from `temp_ids.csv` — 37 prefixes
- [x] Auto-detected FK relationships from `temp_columns.csv` — 609 links
- [x] New web UI tabs: "Detected FKs" and "ID Prefixes"

## Remaining
- [ ] SAP/ERP tables (`mp1.material`, `mp1.mbew`)
- [ ] Organize iMax CSVs into `imports/column-usage/imax/` subfolder

## New Workflow
1. Set `CATALOG` and `SCHEMA` in `schema_analyzer.ipynb`
2. Run all cells (auto-discovers tables)
3. Download ZIP and unzip into `imports/column-usage/<schema>/`
4. Run `python3 scripts/batch_build.py`
5. Run `python3 scripts/build_references.py` (if temp_ids/temp_columns updated)

## Phase 4 Stats
- **Tables:** 49 (4 iMax + 45 sfdcpsa)
- **Columns:** 5,398
- **FK Links:** 609 auto-detected
- **ID Prefixes:** 37

---

# Phase 5: SAP/ERP Tables (Next)

## Objective
Add SAP/ERP tables to complete coverage.

## Data Sources
- [ ] `mp1.material` 
- [ ] `mp1.mbew`
- [ ] Other ERP tables TBD

## Status
Waiting on catalog/schema paths
