#!/usr/bin/env python3
"""
Build ID prefix decoder and auto-detect FK relationships from temp CSV files.

Inputs:
    imports/temp/temp_ids.csv     - Sample IDs per table
    imports/temp/temp_columns.csv - Sample column values

Outputs:
    data/id-prefixes.md  - ID prefix → table mapping
    data/joins.md        - Auto-detected foreign key relationships (appended)
"""

import csv
import re
from pathlib import Path
from datetime import date
from collections import defaultdict

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
TEMP_DIR = PROJECT_ROOT / "imports" / "temp"
DATA_DIR = PROJECT_ROOT / "data"


def extract_sf_prefix(id_value: str) -> str | None:
    """
    Extract Salesforce ID prefix (first 3 chars).
    SF IDs are 15 or 18 characters, alphanumeric.
    """
    if not id_value:
        return None
    # Clean quotes
    id_value = id_value.strip().strip('"')
    # Must be 15 or 18 chars, alphanumeric
    if len(id_value) in (15, 18) and id_value.isalnum():
        return id_value[:3]
    return None


def build_prefix_decoder(ids_path: Path) -> dict[str, list[str]]:
    """
    Parse temp_ids.csv and build prefix → table mapping.
    Returns dict: prefix -> [table_names]
    """
    prefix_map = defaultdict(list)
    
    with open(ids_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            table_name = row.get("table_name", "").strip()
            id_value = row.get("id", "").strip()
            
            prefix = extract_sf_prefix(id_value)
            if prefix and table_name:
                if table_name not in prefix_map[prefix]:
                    prefix_map[prefix].append(table_name)
    
    return dict(prefix_map)


def detect_fk_relationships(columns_path: Path, prefix_map: dict) -> list[dict]:
    """
    Parse temp_columns.csv and detect FK relationships based on ID prefixes.
    Returns list of detected joins.
    """
    relationships = []
    seen = set()  # Dedupe
    
    with open(columns_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            table_name = row.get("table_name", "").strip()
            column_name = row.get("column_name", "").strip()
            column_value = row.get("column_value", "").strip()
            
            # Check if value looks like a Salesforce ID
            prefix = extract_sf_prefix(column_value)
            if not prefix or prefix not in prefix_map:
                continue
            
            # Find target table(s) for this prefix
            target_tables = prefix_map[prefix]
            
            for target_table in target_tables:
                # Skip self-references to own id column
                if table_name == target_table and column_name.lower() == "id":
                    continue
                
                # Create unique key to avoid duplicates
                key = (table_name, column_name, target_table)
                if key in seen:
                    continue
                seen.add(key)
                
                relationships.append({
                    "from_table": table_name,
                    "from_column": column_name,
                    "to_table": target_table,
                    "to_column": "id",
                    "prefix": prefix,
                })
    
    return relationships


def write_prefix_decoder(prefix_map: dict, output_path: Path):
    """Write ID prefix decoder to Markdown file."""
    
    # Sort by prefix
    sorted_prefixes = sorted(prefix_map.items())
    
    lines = [
        "---",
        "type: id-prefixes",
        f"generated_date: {date.today().isoformat()}",
        f"prefix_count: {len(prefix_map)}",
        "---",
        "",
        "# Salesforce ID Prefix Decoder",
        "",
        "Salesforce IDs use a 3-character prefix to identify the object type.",
        "Use this reference to decode IDs and find their source tables.",
        "",
        "## Prefix Reference",
        "",
        "| Prefix | Table(s) | Example |",
        "|--------|----------|---------|",
    ]
    
    for prefix, tables in sorted_prefixes:
        tables_str = ", ".join(f"`{t}`" for t in tables)
        lines.append(f"| `{prefix}` | {tables_str} | |")
    
    lines.extend([
        "",
        "## How to Use",
        "",
        "When you see a Salesforce ID like `001E000001XsEHhIAN`:",
        "1. Take the first 3 characters: `001`",
        "2. Look up in the table above → `imax_account`",
        "3. Query that table with `WHERE id = '001E000001XsEHhIAN'`",
        "",
    ])
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    return output_path


def write_detected_joins(relationships: list[dict], output_path: Path):
    """Write detected FK relationships to Markdown file."""
    
    if not relationships:
        print("No FK relationships detected.")
        return None
    
    # Group by from_table for readability
    by_table = defaultdict(list)
    for rel in relationships:
        by_table[rel["from_table"]].append(rel)
    
    lines = [
        "---",
        "type: auto-detected-joins",
        f"generated_date: {date.today().isoformat()}",
        f"relationship_count: {len(relationships)}",
        "---",
        "",
        "# Auto-Detected Foreign Key Relationships",
        "",
        "These relationships were automatically detected by analyzing sample column values",
        "and matching Salesforce ID prefixes to their source tables.",
        "",
        "## Relationships",
        "",
    ]
    
    for table, rels in sorted(by_table.items()):
        lines.append(f"### {table}")
        lines.append("")
        lines.append("| Column | → | Target Table | Confidence |")
        lines.append("|--------|---|--------------|------------|")
        
        for rel in sorted(rels, key=lambda x: x["from_column"]):
            lines.append(
                f"| `{rel['from_column']}` | → | `{rel['to_table']}`.id | prefix `{rel['prefix']}` |"
            )
        lines.append("")
    
    lines.extend([
        "## Notes",
        "",
        "- These are **inferred** relationships based on ID prefix matching",
        "- Some may be false positives if IDs happen to match patterns",
        "- Review and validate before using in production queries",
        "",
    ])
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    
    return output_path


def main():
    ids_path = TEMP_DIR / "temp_ids.csv"
    columns_path = TEMP_DIR / "temp_columns.csv"
    
    if not ids_path.exists():
        print(f"Error: {ids_path} not found")
        return
    
    print("Building ID Prefix Decoder...")
    print("=" * 60)
    
    # Build prefix decoder
    prefix_map = build_prefix_decoder(ids_path)
    print(f"Found {len(prefix_map)} unique ID prefixes")
    
    # Write decoder
    decoder_path = DATA_DIR / "id-prefixes.md"
    write_prefix_decoder(prefix_map, decoder_path)
    print(f"Written: {decoder_path}")
    
    # Detect FK relationships if columns file exists
    if columns_path.exists():
        print(f"\nDetecting FK Relationships...")
        print("=" * 60)
        
        relationships = detect_fk_relationships(columns_path, prefix_map)
        print(f"Found {len(relationships)} potential FK relationships")
        
        # Write detected joins
        joins_path = DATA_DIR / "detected-joins.md"
        write_detected_joins(relationships, joins_path)
        print(f"Written: {joins_path}")
    
    print("\nDone!")


if __name__ == "__main__":
    main()
