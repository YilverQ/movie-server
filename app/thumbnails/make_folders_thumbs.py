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

def make_folders_thumbs():
    """Crea las carpetas para los thumbnails."""
    print("Folders Thumbnails:")
    create_folder(Config.FOLDER_THUMBNAILS)