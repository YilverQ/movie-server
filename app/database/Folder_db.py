"""
	Folder_db
	--------------------------------------
	get_folders = Método que nos busca únicamente carpetas dentro de una ruta.  
	get_files = Método que nos busca únicamente archivos (Vídeos) de una ruta.
"""
import os
from config import Config

class Folder_DB:
	def get_folders(self, folder = ''):
		folders = []
		location = Config.VIDEO_FOLDER + folder
		for item in os.listdir(location):
			if (not '_' in item) and (not '.' in item):
				folders.append(item)
		folders.sort()
		return folders


	def get_files(self, folder = ''):
		files = []
		location = Config.VIDEO_FOLDER + folder
		for item in os.listdir(location):
			if not ('_' in item) and '.' in item:
				files.append(item)
		files.sort()
		return files