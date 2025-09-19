import yaml
from os.path import splitext, exists, join
from shutil import move


def load_config(path):
    
    with open(path, "r") as f:
        return yaml.safe_load(f)


def make_unique(dest, name):
    """
    Generate a unique filename in the destination folder.

    If a file with the same name exists, appends a counter
    to the filename, e.g., "file.txt" -> "file(1).txt".

    Args:
        dest (str): Destination directory path.
        name (str): Original filename.

    Returns:
        str: Unique filename safe to use in the destination folder.
    """
    filename, extension = splitext(name)
    counter = 1
    new_name = name
    while exists(join(dest, new_name)):
        new_name = f"{filename}({counter}){extension}"
        counter += 1
    return new_name


def move_file(dest, entry, name):
    """
    Move a file to the destination folder safely.

    - Automatically generates a unique filename if the destination
      already contains a file with the same name.
    - Uses shutil.move to handle moving across filesystems.

    Args:
        dest (str): Destination directory path.
        entry (str or Path): Source file path to move.
        name (str): Desired filename in the destination.
    """
    # Always generate a unique name before moving
    unique_name = make_unique(dest, name)
    dest_path = join(dest, unique_name)

    # Move the file to the destination with the unique name
    move(entry, dest_path)
