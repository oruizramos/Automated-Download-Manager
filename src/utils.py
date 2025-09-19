import yaml
import os
from os import rename
from os.path import splitext, exists, join
from shutil import move


def load_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(join(dest, name)):
        name = f"{filename}({counter}){extension}"
        counter += 1
    return name


def move_file(dest, entry, name):
    if exists(join(dest, name)):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)
