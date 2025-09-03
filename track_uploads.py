#!/usr/bin/env python3
"""Track newsletter issues that have been uploaded.

This script compares HTML files in the ``issues`` directory against a
JSON file that records which issue files have already been handled.
New issue files are printed so that they can be uploaded or compiled,
and the JSON file is updated accordingly.
"""
from __future__ import annotations

import json
from pathlib import Path

# File that stores the record of processed issue HTML files
HISTORY_PATH = Path('upload_history.json')


def load_history() -> set[str]:
    """Load the set of previously processed issue files."""
    if HISTORY_PATH.exists():
        try:
            return set(json.loads(HISTORY_PATH.read_text()))
        except json.JSONDecodeError:
            return set()
    return set()


def save_history(history: set[str]) -> None:
    """Persist the history of processed files to ``HISTORY_PATH``."""
    HISTORY_PATH.write_text(
        json.dumps(sorted(history), indent=2) + "\n"
    )


def find_issue_files() -> set[str]:
    """Return the set of newsletter HTML files under ``issues/``."""
    return {
        str(path)
        for path in Path('issues').rglob('*Newsletter.html')
        if path.is_file()
    }


def main() -> None:
    history = load_history()
    current = find_issue_files()
    new_files = sorted(current - history)

    if new_files:
        print("New issue files detected:")
        for file in new_files:
            print(f" - {file}")
        history.update(new_files)
        save_history(history)
    else:
        print("No new issue files found.")


if __name__ == '__main__':
    main()
