from pathlib import Path
import shutil
import argparse

FILE_TYPES = {
    ".pdf": "PDFs",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".txt": "Text",
    ".mp3": "Audio",
}


def organize_folder(folder):
    folder = Path(folder)

    for item in folder.iterdir():

        if not item.is_file():
            continue

        extension = item.suffix.lower()

        if extension not in FILE_TYPES:
            continue

        category = FILE_TYPES[extension]

        destination_folder = folder / category

        destination_folder.mkdir(exist_ok=True)

        shutil.move(
            str(item),
            str(destination_folder / item.name)
        )

    print("Organization complete!")


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "folder",
        help="Folder to organize"
    )

    args = parser.parse_args()

    organize_folder(args.folder)


if __name__ == "__main__":
    main()