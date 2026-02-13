#!/usr/bin/env python3
"""
Batch process: Convert CSVs → Markdown → SQLite → JSON in one command.

Usage:
    python3 batch_build.py                    # Process all CSVs, rebuild everything
    python3 batch_build.py --csv-only         # Only convert new CSVs to Markdown
    python3 batch_build.py --rebuild          # Force rebuild from existing Markdown
"""

import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
IMPORTS_DIR = PROJECT_ROOT / "imports" / "column-usage"
TABLES_DIR = PROJECT_ROOT / "data" / "tables"

def run_script(script_name: str) -> bool:
    """Run a build script and return success status."""
    script_path = SCRIPT_DIR / script_name
    print(f"\n{'='*50}")
    print(f"Running: {script_name}")
    print('='*50)
    
    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=PROJECT_ROOT,
    )
    return result.returncode == 0


def main():
    args = set(sys.argv[1:])
    csv_only = "--csv-only" in args
    rebuild = "--rebuild" in args
    
    # Count inputs (including subfolders)
    csv_count = len(list(IMPORTS_DIR.glob("**/*.csv")))
    md_count = len(list(TABLES_DIR.glob("*.md")))
    
    print(f"Found {csv_count} CSVs in imports/")
    print(f"Found {md_count} Markdown files in data/tables/")
    
    if csv_count == 0 and not rebuild:
        print("\nNo CSVs found. Add files to imports/column-usage/<schema>/ first.")
        print("Example: imports/column-usage/sfdcpsa/*.csv")
        print("Or use --rebuild to regenerate from existing Markdown.")
        sys.exit(1)
    
    success = True
    
    # Step 1: CSV → Markdown
    if csv_count > 0 or not rebuild:
        success = run_script("csv_to_markdown.py") and success
    
    if csv_only:
        print("\n✓ CSV processing complete (--csv-only mode)")
        sys.exit(0 if success else 1)
    
    # Step 2: Markdown → SQLite
    success = run_script("build_db.py") and success
    
    # Step 3: Markdown → JSON
    success = run_script("build_json.py") and success
    
    # Summary
    print("\n" + "="*50)
    if success:
        print("✓ BUILD COMPLETE")
        print("="*50)
        print("\nOutputs:")
        print(f"  SQLite: build/schema.db")
        print(f"  JSON:   build/data.json")
        print(f"\nView UI: python3 -m http.server 8080")
    else:
        print("✗ BUILD FAILED")
        print("="*50)
        sys.exit(1)


if __name__ == "__main__":
    main()
