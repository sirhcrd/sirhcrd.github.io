#!/usr/bin/env python3
"""
Convert column usage CSV files to Markdown table documentation.

Supports CSVs organized by schema in subfolders:
    imports/column-usage/sfdcpsa/*.csv
    imports/column-usage/imax/*.csv

Usage:
    python3 csv_to_markdown.py                    # Process all CSVs in all subfolders
    python3 csv_to_markdown.py path/to/file.csv   # Process single file
"""

import csv
import os
import sys
from datetime import date
from pathlib import Path

# Paths relative to script location
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
IMPORTS_DIR = PROJECT_ROOT / "imports" / "column-usage"
OUTPUT_DIR = PROJECT_ROOT / "data" / "tables"


def classify_quality(usage_pct: float) -> str:
    """Classify column quality based on usage percentage."""
    if usage_pct >= 50:
        return "trusted"
    elif usage_pct >= 5:
        return "neutral"
    else:
        return "dead"


def extract_table_name(filename: str) -> str:
    """Extract table name from CSV filename.
    
    psa_checklist_c_column_usage.csv -> psa_checklist_c
    columnUsage-imax_case.csv -> imax_case
    """
    name = filename
    # Handle various filename patterns
    name = name.replace("columnUsage-", "")
    name = name.replace("_column_usage", "")
    name = name.replace(".csv", "")
    return name


def get_source_from_path(csv_path: Path) -> str:
    """Get source/schema name from CSV path.
    
    imports/column-usage/sfdcpsa/foo.csv -> sfdcpsa
    imports/column-usage/foo.csv -> unknown
    """
    # Check if parent is a schema subfolder (not the column-usage folder itself)
    if csv_path.parent.name != "column-usage":
        return csv_path.parent.name
    return "unknown"


def parse_number(value: str) -> int:
    """Parse number that may contain commas."""
    return int(value.replace(",", ""))


def convert_csv_to_markdown(csv_path: Path, output_dir: Path, source: str = None) -> Path:
    """Convert a single CSV file to Markdown format."""
    table_name = extract_table_name(csv_path.name)
    
    # Determine source from path if not provided
    if source is None:
        source = get_source_from_path(csv_path)
    
    output_path = output_dir / f"{table_name}.md"
    
    # Read CSV data
    columns = []
    total_rows = 0
    
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            usage_pct = float(row["Usage %"])
            columns.append({
                "name": row["Column"],
                "usage_pct": usage_pct,
                "empty_pct": float(row["Empty %"]),
                "quality": classify_quality(usage_pct),
            })
            # Get total rows from first row (same for all)
            if total_rows == 0:
                total_rows = parse_number(row["Total Rows"])
    
    # Sort by usage descending (most useful columns first)
    columns.sort(key=lambda x: x["usage_pct"], reverse=True)
    
    # Count by quality
    quality_counts = {"trusted": 0, "neutral": 0, "dead": 0}
    for col in columns:
        quality_counts[col["quality"]] += 1
    
    # Generate Markdown
    md_lines = [
        "---",
        f"table: {table_name}",
        f"source: {source}",
        f"pulled_date: {date.today().isoformat()}",
        f"row_count: {total_rows}",
        f"column_count: {len(columns)}",
        "---",
        "",
        f"# {table_name}",
        "",
        "*Description needed — add context about what this table represents.*",
        "",
        "## Summary",
        "",
        f"| Quality | Count | Percentage |",
        f"|---------|-------|------------|",
        f"| Trusted (≥50%) | {quality_counts['trusted']} | {quality_counts['trusted']*100//len(columns)}% |",
        f"| Neutral (5-50%) | {quality_counts['neutral']} | {quality_counts['neutral']*100//len(columns)}% |",
        f"| Dead (<5%) | {quality_counts['dead']} | {quality_counts['dead']*100//len(columns)}% |",
        "",
        "## Columns",
        "",
        "| Column | Usage % | Quality | Description |",
        "|--------|---------|---------|-------------|",
    ]
    
    for col in columns:
        # Escape pipe characters in column names
        col_name = col["name"].replace("|", "\\|")
        md_lines.append(
            f"| `{col_name}` | {col['usage_pct']:.1f}% | {col['quality']} | |"
        )
    
    md_lines.extend([
        "",
        "## Notes",
        "",
        "*Add join information, gotchas, and usage patterns here.*",
        "",
    ])
    
    # Write output
    output_dir.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    
    return output_path


def main():
    """Process CSV files and generate Markdown."""
    if len(sys.argv) > 1:
        # Process specific file
        csv_files = [Path(sys.argv[1])]
    else:
        # Process all CSVs in imports directory and subdirectories
        # Skip summary files (start with _)
        csv_files = [f for f in IMPORTS_DIR.glob("**/*.csv") if not f.name.startswith("_")]
    
    if not csv_files:
        print(f"No CSV files found in {IMPORTS_DIR}")
        print("Expected structure: imports/column-usage/<schema>/*.csv")
        sys.exit(1)
    
    # Group by source for reporting
    by_source = {}
    for csv_path in csv_files:
        source = get_source_from_path(csv_path)
        by_source.setdefault(source, []).append(csv_path)
    
    print(f"Processing {len(csv_files)} CSV file(s) from {len(by_source)} source(s)...")
    
    for source, files in sorted(by_source.items()):
        print(f"\n[{source}] - {len(files)} tables")
        for csv_path in files:
            output_path = convert_csv_to_markdown(csv_path, OUTPUT_DIR, source)
            print(f"  {csv_path.name} -> {output_path.name}")
    
    print(f"\nGenerated {len(csv_files)} Markdown file(s) in {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
