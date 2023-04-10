import os
from ..thumbnails.thumbnails import *
from config import Config

URL_VIDEOS = Config.VIDEO_FOLDER
URL_THUMBNAILS = os.getcwd() + '/' + Config.FOLDER_THUMBNAILS

def make_thumbnails():
	thumbnail = Thumbnails()
	for folderName, subfolders, filenames in os.walk(URL_VIDEOS):
		if folderName[-1:] == "_":
			continue
		print('The current folder is ' + folderName)
	 
		for subfolder in subfolders:
			folder_ubication = folderName.replace(URL_VIDEOS, URL_THUMBNAILS)
			if subfolder[-1:] == "_":
				continue
			
			if not (os.path.exists(f'{folder_ubication}/{subfolder}')):
				print(thumbnail.make_folder(subfolder, folder_ubication))
				continue
			print(f"Folder already exists ({subfolder})")
	 	
		for file in filenames:
			folder_ubication = folderName.replace(URL_VIDEOS, URL_THUMBNAILS)
			if os.path.exists(f'{folder_ubication}/{file[:-4]}.jpg'):
				print(f"File already exists ({file})")
				continue

			try:
				image_thumbnail = thumbnail.make_thumbnail(file, folderName)
				image   = thumbnail.make_thumbnail_image(image_thumbnail)
				image   = thumbnail.resize_image(image, width = 350, height = 200)
				message = thumbnail.save_image(image, folder_ubication, file)
				print(message)
			except:
				error_message = f'Ha ocurrido un error con el archivo: {file}'
				print(error_message)
		print('')


def mostrar():
	print(URL_VIDEOS)
	print(URL_THUMBNAILS)