import os
import pytest
from pathlib import Path
from src.utils import make_unique, move_file


def test_make_unique(tmp_path):
    dest = tmp_path
    file_path = dest / "file.txt"
    file_path.write_text("content")

    unique_name = make_unique(dest, "file.txt")
    assert unique_name.startswith("file(")
    assert unique_name.endswith(").txt")


def test_move_file(tmp_path):
    # Create a destination folder
    dest = tmp_path / "dest"
    dest.mkdir()

    # Create a dummy file to "move"
    src_file = tmp_path / "test.txt"
    src_file.write_text("hello")

    # Call move_file
    move_file(str(dest), str(src_file), "test.txt")

    # File should now exist in destination
    moved_file = dest / "test.txt"
    assert moved_file.exists()
    assert moved_file.read_text() == "hello"
