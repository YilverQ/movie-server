"""
	Folder_db
	--------------------------------------
	get_folders = Método que nos busca únicamente carpetas dentro de una ruta.  
	get_files = Método que nos busca únicamente archivos (Vídeos) de una ruta.
"""
import os
from config import Config

class Folder_DB:
	def get_folders(self, folder=''):
	    location = os.path.join(Config.VIDEO_FOLDER, folder)
	    #listar solamente las carpetas
	    folders = [item for item in os.listdir(location) if os.path.isdir(os.path.join(location, item))]
	    folders.sort()
	    return folders


	def get_files(self, folder=''):
	    location = os.path.join(Config.VIDEO_FOLDER, folder)
	    files = [item for item in os.listdir(location) if os.path.isfile(os.path.join(location, item))]
	    files.sort()
	    return files