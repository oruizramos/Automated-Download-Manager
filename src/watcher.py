import logging
from os import scandir
from src.organizer import FileOrganizer
from watchdog.events import FileSystemEventHandler


class FileEventHandler(FileSystemEventHandler):
    def __init__(self, config):
        super().__init__()
        self.organizer = FileOrganizer(config)

    def on_modified(self, event):
        # Reacts whenever a file/folder is modified in the source directory
        with scandir(self.organizer.source_dir) as entries:
            for entry in entries:
                self.organizer.handle_file(entry)
                logging.info(f"Processed file event: {entry.name}")



