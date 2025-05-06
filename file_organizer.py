import os
import shutil
from pathlib import Path

# Define the folder you want to organize
# Change this to any folder you want to organize
DOWNLOADS_FOLDER = Path.home() / "AppData//Local//Programs//data"
# DOWNLOADS_FOLDER = Path.home() 
print("this is path :   ", DOWNLOADS_FOLDER)

# Define the folder categories and associated file types
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".mkv"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"],
}