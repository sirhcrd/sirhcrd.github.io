#!/usr/bin/env python3
"""
Build JSON data file for web UI from Markdown table documentation.

Usage:
    python3 build_json.py
"""

import json
import re
from pathlib import Path

# Paths relative to script location
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
TABLES_DIR = PROJECT_ROOT / "data" / "tables"
JOINS_FILE = PROJECT_ROOT / "data" / "joins.md"
DETECTED_JOINS_FILE = PROJECT_ROOT / "data" / "detected-joins.md"
ID_PREFIXES_FILE = PROJECT_ROOT / "data" / "id-prefixes.md"
GLOSSARY_FILE = PROJECT_ROOT / "data" / "glossary.md"
BUILD_DIR = PROJECT_ROOT / "build"
OUTPUT_PATH = BUILD_DIR / "data.json"

# Regex patterns
FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
COLUMN_ROW_PATTERN = re.compile(
    r"^\|\s*`([^`]+)`\s*\|\s*([\d.]+)%\s*\|\s*(\w+)\s*\|\s*(.*?)\s*\|$"
)


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from Markdown content."""
    match = FRONTMATTER_PATTERN.match(content)
    if not match:
        return {}
    
    frontmatter = {}
    for line in match.group(1).split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            frontmatter[key.strip()] = value.strip()
    return frontmatter


def parse_columns(content: str) -> list[dict]:
    """Extract column data from Markdown table."""
    columns = []
    for line in content.split("\n"):
        match = COLUMN_ROW_PATTERN.match(line.strip())
        if match:
            columns.append({
                "name": match.group(1),
                "usage_pct": float(match.group(2)),
                "quality": match.group(3),
                "description": match.group(4).strip() or None,
            })
    return columns


def parse_description(content: str) -> str | None:
    """Extract table description from Markdown."""
    # Look for first paragraph after the title
    match = re.search(r"^# .+\n\n(.+?)(?:\n\n|$)", content, re.MULTILINE)
    if match:
        desc = match.group(1).strip()
        if not desc.startswith("*"):  # Skip placeholder text
            return desc
    return None


def load_table(md_path: Path) -> dict | None:
    """Load a single table Markdown file."""
    content = md_path.read_text(encoding="utf-8")
    meta = parse_frontmatter(content)
    
    if not meta.get("table"):
        return None
    
    columns = parse_columns(content)
    
    # Count by quality
    quality_counts = {"trusted": 0, "neutral": 0, "dead": 0}
    for col in columns:
        quality_counts[col["quality"]] += 1
    
    return {
        "name": meta.get("table"),
        "source": meta.get("source"),
        "pulled_date": meta.get("pulled_date"),
        "row_count": int(meta.get("row_count", 0)) if meta.get("row_count") else None,
        "column_count": int(meta.get("column_count", 0)) if meta.get("column_count") else len(columns),
        "description": parse_description(content),
        "quality_summary": quality_counts,
        "columns": columns,
    }


def parse_joins(joins_path: Path) -> list[dict]:
    """Parse join definitions from joins.md."""
    if not joins_path.exists():
        return []
    
    content = joins_path.read_text(encoding="utf-8")
    joins = []
    
    # Split by ## headers
    sections = re.split(r"(?=^### )", content, flags=re.MULTILINE)
    
    for section in sections:
        # Match header like "### table_a → table_b"
        header_match = re.match(r"^### (\S+)\s*→\s*(\S+)", section)
        if not header_match:
            continue
        
        from_table = header_match.group(1)
        to_table = header_match.group(2)
        
        join_data = {
            "from_table": from_table,
            "to_table": to_table,
            "join_column": None,
            "join_type": None,
            "cardinality": None,
            "notes": None,
        }
        
        for line in section.split("\n"):
            line = line.strip()
            if line.startswith("- **Join column"):
                match = re.search(r":\*\*\s*(.+)", line)
                if match:
                    join_data["join_column"] = match.group(1).strip()
            elif line.startswith("- **Type"):
                match = re.search(r":\*\*\s*(.+)", line)
                if match:
                    join_data["join_type"] = match.group(1).strip()
            elif line.startswith("- **Cardinality"):
                match = re.search(r":\*\*\s*(.+)", line)
                if match:
                    join_data["cardinality"] = match.group(1).strip()
            elif line.startswith("- **Notes"):
                match = re.search(r":\*\*\s*(.+)", line)
                if match:
                    join_data["notes"] = match.group(1).strip()
        
        joins.append(join_data)
    
    return joins


def parse_glossary(glossary_path: Path) -> list[dict]:
    """Parse glossary from glossary.md."""
    if not glossary_path.exists():
        return []
    
    content = glossary_path.read_text(encoding="utf-8")
    glossary = []
    
    # Find markdown table rows
    for line in content.split("\n"):
        # Match table rows like "| Term | `technical` | Description |"
        match = re.match(r"^\|\s*([^|]+)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+)\s*\|$", line)
        if match:
            term = match.group(1).strip()
            technical = match.group(2).strip()
            description = match.group(3).strip()
            if term and term != "Term":  # Skip header
                glossary.append({
                    "term": term,
                    "technical": technical,
                    "description": description,
                })
    
    return glossary


def parse_id_prefixes(prefixes_path: Path) -> list[dict]:
    """Parse ID prefix decoder from id-prefixes.md."""
    if not prefixes_path.exists():
        return []
    
    content = prefixes_path.read_text(encoding="utf-8")
    prefixes = []
    
    # Find markdown table rows like "| `001` | `imax_account`, `ipsa_account` | |"
    for line in content.split("\n"):
        match = re.match(r"^\|\s*`([^`]+)`\s*\|\s*(.+?)\s*\|\s*.*\|$", line)
        if match:
            prefix = match.group(1).strip()
            tables_str = match.group(2).strip()
            if prefix and prefix != "Prefix":  # Skip header
                # Parse tables from backtick-wrapped list
                tables = re.findall(r"`([^`]+)`", tables_str)
                prefixes.append({
                    "prefix": prefix,
                    "tables": tables,
                })
    
    return prefixes


def parse_detected_joins(joins_path: Path) -> list[dict]:
    """Parse auto-detected joins from detected-joins.md."""
    if not joins_path.exists():
        return []
    
    content = joins_path.read_text(encoding="utf-8")
    joins = []
    current_table = None
    
    for line in content.split("\n"):
        # Match section headers like "### imax_case_line"
        header_match = re.match(r"^### (\S+)", line)
        if header_match:
            current_table = header_match.group(1)
            continue
        
        # Match table rows like "| `column` | → | `target`.id | prefix `001` |"
        row_match = re.match(
            r"^\|\s*`([^`]+)`\s*\|\s*→\s*\|\s*`([^`]+)`\.id\s*\|\s*prefix\s*`([^`]+)`\s*\|$",
            line
        )
        if row_match and current_table:
            joins.append({
                "from_table": current_table,
                "from_column": row_match.group(1),
                "to_table": row_match.group(2),
                "to_column": "id",
                "prefix": row_match.group(3),
                "confidence": "auto-detected",
            })
    
    return joins


def main():
    """Build JSON data file from Markdown sources."""
    # Load all tables
    table_files = list(TABLES_DIR.glob("*.md"))
    tables = []
    
    for md_path in sorted(table_files):
        table_data = load_table(md_path)
        if table_data:
            tables.append(table_data)
    
    # Load manual joins
    joins = parse_joins(JOINS_FILE)
    
    # Load auto-detected joins
    detected_joins = parse_detected_joins(DETECTED_JOINS_FILE)
    
    # Load ID prefixes
    id_prefixes = parse_id_prefixes(ID_PREFIXES_FILE)
    
    # Load glossary
    glossary = parse_glossary(GLOSSARY_FILE)
    
    # Build output
    data = {
        "generated": str(Path(__file__).stat().st_mtime),
        "tables": tables,
        "joins": joins,
        "detected_joins": detected_joins,
        "id_prefixes": id_prefixes,
        "glossary": glossary,
        "stats": {
            "table_count": len(tables),
            "column_count": sum(t["column_count"] for t in tables),
            "join_count": len(joins),
            "detected_join_count": len(detected_joins),
            "prefix_count": len(id_prefixes),
        }
    }
    
    # Write output
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    
    print(f"Generated {OUTPUT_PATH}")
    print(f"  Tables: {len(tables)}")
    print(f"  Columns: {data['stats']['column_count']}")
    print(f"  Manual Joins: {len(joins)}")
    print(f"  Detected Joins: {len(detected_joins)}")
    print(f"  ID Prefixes: {len(id_prefixes)}")


if __name__ == "__main__":
    main()
