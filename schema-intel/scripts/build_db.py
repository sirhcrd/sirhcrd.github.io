#!/usr/bin/env python3
"""
Build SQLite database from Markdown table documentation.

Usage:
    python3 build_db.py              # Build from all Markdown files
    python3 build_db.py --clean      # Delete existing DB first
"""

import re
import sqlite3
import sys
from pathlib import Path

# Paths relative to script location
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
TABLES_DIR = PROJECT_ROOT / "data" / "tables"
JOINS_FILE = PROJECT_ROOT / "data" / "joins.md"
BUILD_DIR = PROJECT_ROOT / "build"
DB_PATH = BUILD_DIR / "schema.db"

# Regex patterns for parsing Markdown
FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
COLUMN_ROW_PATTERN = re.compile(
    r"^\|\s*`([^`]+)`\s*\|\s*([\d.]+)%\s*\|\s*(\w+)\s*\|\s*(.*?)\s*\|$"
)
JOIN_SECTION_PATTERN = re.compile(
    r"^##\s+(\w+)\s*→\s*(\w+)", re.MULTILINE
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


def parse_joins(content: str) -> list[dict]:
    """Extract join definitions from joins.md."""
    joins = []
    sections = re.split(r"(?=^## )", content, flags=re.MULTILINE)
    
    for section in sections:
        # Match section header like "## imax_case → zone_mapping"
        header_match = JOIN_SECTION_PATTERN.match(section)
        if not header_match:
            continue
        
        from_table = header_match.group(1)
        to_table = header_match.group(2)
        
        # Extract metadata from bullet points
        join_data = {
            "from_table": from_table,
            "to_table": to_table,
            "from_column": None,
            "to_column": None,
            "join_type": None,
            "cardinality": None,
            "notes": None,
        }
        
        for line in section.split("\n"):
            line = line.strip()
            if line.startswith("- **Join column"):
                # Extract column name(s)
                match = re.search(r":\*\*\s*(.+)", line)
                if match:
                    col = match.group(1).strip()
                    join_data["from_column"] = col
                    join_data["to_column"] = col  # Assume same name unless specified
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


def create_database(db_path: Path) -> sqlite3.Connection:
    """Create SQLite database with schema."""
    db_path.parent.mkdir(parents=True, exist_ok=True)
    
    conn = sqlite3.connect(db_path)
    conn.executescript("""
        DROP TABLE IF EXISTS columns;
        DROP TABLE IF EXISTS tables;
        DROP TABLE IF EXISTS joins;
        DROP TABLE IF EXISTS id_prefixes;
        
        CREATE TABLE tables (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            source TEXT,
            description TEXT,
            row_count INTEGER,
            column_count INTEGER,
            pulled_date TEXT
        );
        
        CREATE TABLE columns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            table_id INTEGER REFERENCES tables(id),
            name TEXT NOT NULL,
            data_type TEXT,
            usage_pct REAL,
            quality TEXT,
            description TEXT,
            UNIQUE(table_id, name)
        );
        
        CREATE TABLE joins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            from_table TEXT NOT NULL,
            from_column TEXT,
            to_table TEXT NOT NULL,
            to_column TEXT,
            join_type TEXT,
            cardinality TEXT,
            notes TEXT
        );
        
        CREATE TABLE id_prefixes (
            prefix TEXT PRIMARY KEY,
            object_name TEXT,
            description TEXT
        );
        
        CREATE INDEX idx_columns_table ON columns(table_id);
        CREATE INDEX idx_columns_name ON columns(name);
        CREATE INDEX idx_columns_quality ON columns(quality);
        CREATE INDEX idx_joins_from ON joins(from_table);
        CREATE INDEX idx_joins_to ON joins(to_table);
    """)
    
    return conn


def load_table(conn: sqlite3.Connection, md_path: Path) -> int:
    """Load a single table Markdown file into the database."""
    content = md_path.read_text(encoding="utf-8")
    
    # Parse frontmatter
    meta = parse_frontmatter(content)
    if not meta.get("table"):
        print(f"  Warning: {md_path.name} has no 'table' in frontmatter, skipping")
        return 0
    
    # Extract description (first paragraph after title)
    desc_match = re.search(r"^# .+\n\n(.+?)(?:\n\n|$)", content, re.MULTILINE)
    description = desc_match.group(1) if desc_match else None
    
    # Insert table record
    cursor = conn.execute(
        """
        INSERT INTO tables (name, source, description, row_count, column_count, pulled_date)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            meta.get("table"),
            meta.get("source"),
            description,
            int(meta.get("row_count", 0)) if meta.get("row_count") else None,
            int(meta.get("column_count", 0)) if meta.get("column_count") else None,
            meta.get("pulled_date"),
        ),
    )
    table_id = cursor.lastrowid
    
    # Parse and insert columns
    columns = parse_columns(content)
    for col in columns:
        conn.execute(
            """
            INSERT INTO columns (table_id, name, usage_pct, quality, description)
            VALUES (?, ?, ?, ?, ?)
            """,
            (table_id, col["name"], col["usage_pct"], col["quality"], col["description"]),
        )
    
    return len(columns)


def load_joins(conn: sqlite3.Connection, joins_path: Path) -> int:
    """Load join definitions from joins.md."""
    if not joins_path.exists():
        return 0
    
    content = joins_path.read_text(encoding="utf-8")
    joins = parse_joins(content)
    
    for join in joins:
        conn.execute(
            """
            INSERT INTO joins (from_table, from_column, to_table, to_column, join_type, cardinality, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                join["from_table"],
                join["from_column"],
                join["to_table"],
                join["to_column"],
                join["join_type"],
                join["cardinality"],
                join["notes"],
            ),
        )
    
    return len(joins)


def main():
    """Build SQLite database from Markdown files."""
    # Handle --clean flag
    if "--clean" in sys.argv and DB_PATH.exists():
        DB_PATH.unlink()
        print(f"Deleted existing database: {DB_PATH}")
    
    # Check for table files
    table_files = list(TABLES_DIR.glob("*.md"))
    if not table_files:
        print(f"No Markdown files found in {TABLES_DIR}")
        print("Run csv_to_markdown.py first to generate table files.")
        sys.exit(1)
    
    print(f"Building database from {len(table_files)} table file(s)...")
    
    # Create database
    conn = create_database(DB_PATH)
    
    # Load tables
    total_columns = 0
    for md_path in sorted(table_files):
        col_count = load_table(conn, md_path)
        print(f"  {md_path.name}: {col_count} columns")
        total_columns += col_count
    
    # Load joins
    join_count = load_joins(conn, JOINS_FILE)
    if join_count:
        print(f"  joins.md: {join_count} relationships")
    
    conn.commit()
    conn.close()
    
    print(f"\nDatabase built: {DB_PATH}")
    print(f"  Tables: {len(table_files)}")
    print(f"  Columns: {total_columns}")
    print(f"  Joins: {join_count}")


if __name__ == "__main__":
    main()
