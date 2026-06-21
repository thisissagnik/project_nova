#!/usr/bin/env python3
"""Update the 'Last updated' line in docs/project_docs/PROJECT_STATUS.md.

Usage: python scripts/update_status.py
This is intended to be run by the assistant after completing tracked changes.
"""
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS_PATH = ROOT / "docs" / "project_docs" / "PROJECT_STATUS.md"


def update_last_updated(dt: date) -> None:
    if not STATUS_PATH.exists():
        raise SystemExit(f"Status file not found: {STATUS_PATH}")

    text = STATUS_PATH.read_text(encoding="utf-8")
    lines = text.splitlines()

    # Replace the first occurrence of a line that starts with 'Last updated:'
    for i, line in enumerate(lines[:10]):
        if line.strip().lower().startswith("last updated:"):
            lines[i] = f"Last updated: {dt.isoformat()}"
            break
    else:
        # If not found, insert after the title line if present
        insert_at = 1 if len(lines) > 1 else 0
        lines.insert(insert_at, f"Last updated: {dt.isoformat()}")

    STATUS_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    update_last_updated(date.today())
