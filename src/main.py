import logging
from time import sleep
from watchdog.observers import Observer
from src.watcher import FileEventHandler
from src.utils import load_config


def main():
    # Load configuration from YAML
    config = load_config("config.yaml")

    source_dir = config["watch_directory"]

    # Set up logging to console
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    event_handler = FileEventHandler(config)
    observer = Observer()
    observer.schedule(event_handler, source_dir, recursive=True)
    observer.start()

    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


if __name__ == "__main__":
    main()
