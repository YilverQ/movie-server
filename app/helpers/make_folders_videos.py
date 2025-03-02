import os
from config import Config

# Constantes para los nombres de las carpetas
FOLDER_NAMES = ["Animes", "Películas", "Series"]

def create_folder(route):
    """Crea una carpeta si no existe."""
    if not os.path.exists(route):
        os.makedirs(route, exist_ok=True)
        print(f"Folder created: {route}")
    else:
        print(f"Folder already exists: {route}")

def make_folders_videos():
    """Crea las carpetas para los thumbnails."""
    print("Folders To Videos:")
    create_folder(Config.VIDEO_FOLDER)
    for folder in FOLDER_NAMES:
        route = os.path.join(Config.VIDEO_FOLDER, folder)
        create_folder(route)