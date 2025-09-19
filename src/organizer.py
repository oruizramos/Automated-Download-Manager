import logging
from os.path import splitext
from src.utils import move_file


class FileOrganizer:
    # Supported file extensions by category
    IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif", ".webp", ".tiff", ".bmp", ".svg", ".ico"]
    THREED_EXTENSIONS = [".stl", ".obj", ".fbx", ".gltf", ".dae", ".3ds"]
    VIDEO_EXTENSIONS = [".webm", ".mpg", ".mpeg", ".mp4", ".avi", ".wmv", ".mov", ".flv", ".r3d", ".mxf"]
    AUDIO_EXTENSIONS = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac", ".aiff", ".aif", ".bwf"]
    DOCUMENT_EXTENSIONS = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]

    def __init__(self, config):
        self.source_dir = config["watch_directory"]
        self.dest_dirs = config["destination_directories"]

    def handle_file(self, entry):
        name = entry.name.lower()

        if any(name.endswith(ext) for ext in self.AUDIO_EXTENSIONS):
            if entry.stat().st_size < 10_000_000 or "sfx" in name:
                dest = self.dest_dirs["sfx"]
            else:
                dest = self.dest_dirs["music"]
            move_file(dest, entry, entry.name)
            logging.info(f"Moved audio file: {entry.name}")

        elif any(name.endswith(ext) for ext in self.VIDEO_EXTENSIONS):
            move_file(self.dest_dirs["videos"], entry, entry.name)
            logging.info(f"Moved video file: {entry.name}")

        elif any(name.endswith(ext) for ext in self.IMAGE_EXTENSIONS):
            move_file(self.dest_dirs["images"], entry, entry.name)
            logging.info(f"Moved image file: {entry.name}")

        elif any(name.endswith(ext) for ext in self.DOCUMENT_EXTENSIONS):
            move_file(self.dest_dirs["documents"], entry, entry.name)
            logging.info(f"Moved document file: {entry.name}")

        elif any(name.endswith(ext) for ext in self.THREED_EXTENSIONS):
            move_file(self.dest_dirs.get("models", self.dest_dirs["documents"]), entry, entry.name)
            logging.info(f"Moved 3D model file: {entry.name}")
