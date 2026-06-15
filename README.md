# File Organizer CLI

A Python command-line tool that automatically organizes files into categorized folders based on their file extensions.

## Overview

This project scans a specified directory, identifies files by their extensions, creates category folders if they do not already exist, and moves files into their appropriate locations.

For example:

### Before

```text
Downloads/
│
├── report.pdf
├── image.jpg
├── notes.txt
└── song.mp3
```

### After

```text
Downloads/
│
├── PDFs/
│   └── report.pdf
│
├── Images/
│   └── image.jpg
│
├── Text/
│   └── notes.txt
│
└── Audio/
    └── song.mp3
```

---

## Features

- Automatically categorizes files by extension
- Creates destination folders automatically
- Supports command-line usage
- Uses modern Python libraries (`pathlib`, `argparse`)
- Simple and lightweight
- Cross-platform (Windows, Linux, macOS)

---

## Supported File Types

| Extension | Category |
|------------|-----------|
| .pdf | PDFs |
| .jpg | Images |
| .jpeg | Images |
| .png | Images |
| .txt | Text |
| .mp3 | Audio |

Additional file types can be added easily by modifying the `FILE_TYPES` dictionary.

---

## Project Structure

```text
file_organizer/
│
├── src/
│   └── organizer/
│       ├── __init__.py
│       └── main.py
│
├── tests/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Requirements

- Python 3.8+
- Standard Library Only

No external packages are required.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/file-organizer-cli.git
cd file-organizer-cli
```

### Create Virtual Environment

Windows CMD:

```cmd
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python -m venv venv
source venv/bin/activate
```

---

## Usage

Run the script and provide the folder path you want to organize.

### Example

```cmd
python src\organizer\main.py Downloads
```

or

```cmd
python src\organizer\main.py C:\Users\YourName\Downloads
```

---

## Example Output

```text
Organization complete!
```

---

## How It Works

1. Reads the target directory provided by the user.
2. Iterates through all files in the directory.
3. Detects each file's extension.
4. Matches the extension to a predefined category.
5. Creates the category folder if necessary.
6. Moves the file into the corresponding folder.

---

## Technologies Used

- Python
- pathlib
- shutil
- argparse
- Git
- GitHub

---

## Future Improvements

Potential enhancements include:

- Support for additional file types
- Logging system
- Duplicate file detection
- Recursive folder organization
- GUI version using Tkinter or PyQt
- Packaging as an installable Python CLI tool
- Unit tests using pytest

---

## Learning Outcomes

This project demonstrates:

- File system automation
- Command-line interface development
- Python project organization
- Virtual environments
- Git and GitHub workflows
- Usage of Python standard library modules

---

## Author

Created as a Python automation project to practice:

- Python fundamentals
- CLI development
- File handling
- Git and GitHub
- Professional project structure

---