import os
import pytest
from src.utils import make_unique, move_file


def test_make_unique(tmp_path):
    """Ensure make_unique generates a new name if file already exists."""
    dest = tmp_path
    file_path = dest / "file.txt"
    file_path.write_text("content")

    unique_name = make_unique(dest, "file.txt")

    # Rename to file(1).txt or similar
    assert unique_name.startswith("file(")
    assert unique_name.endswith(").txt")
    assert unique_name != "file.txt"


def test_move_file_creates_unique(tmp_path):
    """Ensure move_file does not overwrite and moves with unique name."""
    # Setup: create destination + conflicting file
    dest = tmp_path
    existing_file = dest / "file.txt"
    existing_file.write_text("existing content")

    # Create a new file to move
    new_file = tmp_path / "new_file.txt"
    new_file.write_text("new content")

    # Act: try moving into the same folder with conflicting name
    move_file(dest, new_file, "file.txt")

    # Assert: both files exist (original + renamed one)
    files = list(dest.iterdir())
    names = [f.name for f in files]

    assert "file.txt" in names
    assert any(name.startswith("file(") and name.endswith(").txt") for name in names)
