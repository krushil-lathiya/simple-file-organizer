import os
import shutil
from pathlib import Path

# Define the folder you want to organize
# Change this to any folder you want to organize
DOWNLOADS_FOLDER = Path.home() / "AppData//Local//Programs//data"
# DOWNLOADS_FOLDER = Path.home() 
# print("this is path :   ", DOWNLOADS_FOLDER)

# Define the folder categories and associated file types
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"],
}

def organize_files(folder):

    for file in os.listdir(folder):
        file_path = folder / file

        # Skip if it's a directory
        if file_path.is_dir():
            continue

        # Get the file extension
        ext = file_path.suffix.lower()

        # Find the right folder category
        moved = False
        for category, extensions in FILE_TYPES.items():
            if ext in extensions:
                category_folder = folder / category
                category_folder.mkdir(exist_ok=True)  # Create folder if it doesn't exist
                shutil.move(str(file_path), str(category_folder / file))
                moved = True
                print(f"Moved {file} to {category}/")
                break

        # If the file didn't match any category
        if not moved:
            other_folder = folder / "Others"
            other_folder.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(other_folder / file))
            print(f"Moved {file} to Others/")

# Run the organizer
organize_files(DOWNLOADS_FOLDER)