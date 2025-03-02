import os
from .thumbnails import Thumbnails
from config import Config

URL_VIDEOS = Config.VIDEO_FOLDER
URL_THUMBNAILS = Config.FOLDER_THUMBNAILS

def make_thumbnails():
	thumbnail = Thumbnails()
	for folderName, subfolders, filenames in os.walk(URL_VIDEOS):
		print('The current folder is ' + folderName)
			 
		for subfolder in subfolders:
			folder_ubication = folderName.replace(URL_VIDEOS, URL_THUMBNAILS)
			folder_ubication_thumb = os.path.join(folder_ubication, subfolder)
			thumbnail.make_folder(folder_ubication_thumb)
	 	
		for file in filenames:
			folder_ubication = folderName.replace(URL_VIDEOS, URL_THUMBNAILS)
			file_thumb = os.path.join(folder_ubication, file)
			
			if thumbnail.is_thumb_exist(file_thumb):
				print(f"File already exists: {file}")
				continue

			try:
				image_thumbnail = thumbnail.make_thumbnail(folderName, file)
				image   = thumbnail.make_thumbnail_image(image_thumbnail)
				image   = thumbnail.resize_image(image, width = 350, height = 200)
				message = thumbnail.save_image(image, folder_ubication, file)
				print(message)
			except:
				path_file = os.path.join(folderName, file)
				error_message = f'Error with file: {path_file}'
				print(f"\033[91m{error_message}\033[0m")
		print('')