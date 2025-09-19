# Automated Download Manager

A file automation tool that monitors a directory (e.g., your Downloads folder) and automatically organizes files into categorized subfolders. (Images, 3D models, Videos, Music, SFX, and Documents).

It started as a way to explore Python automation/testing while being somewhat useful to my video/audio editing and 3D modeling hobbyst workflow.

## What it does
- Real-time file monitoring using watchdog
- Automatic file moving and renaming (prevents overwrites)
- YAML configuration for flexible setup
- Logging of all actions
- Unit tests included with pytest
- Continuous Integration via GitHub Actions (runs tests on every Push/Pull Request)

## Setup
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/auto_organizer.git
   cd auto_organizer
   ```

2. Install requirements:
   ```
   pip install -r requirements.txt
   ```

3. Copy `config.example.yaml` to `config.yaml` and adjust paths:
   ```
   cp config.example.yaml config.yaml
   ```

4. Run the organizer:

   ```
   python -m src.main
   ```

5. Build (Optional. To createe a standalone executable with PyInstaller)

```
pip install pyinstaller
pyinstaller --onefile src/main.py
```

## Tests
Run unit tests with:

```
pytest tests/
```

## Github Actions CI

Workflow (.github/workflows/python-app.yml) will automatically:

-Set up Python 3.11
-Install dependencies
-Runs all tests with pytest

Test results can be seen directly in the GitHub Actions tab of the repository.