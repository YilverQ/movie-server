#Importando Librerías
from moviepy.editor import *
from PIL import Image
import os

"""
	Creamos una clase llamada Thumbnails que contendrá 
	todos los métodos necesarios para crear 
	archivos thumbnails
"""
class Thumbnails():
	#__ Método para crear carpetas __#
	def make_folder(self, folder_ubication_thumb):
		if not (os.path.exists(folder_ubication_thumb)):
			create_folder = os.makedirs(folder_ubication_thumb, exist_ok = True)
			print(f"Folder thumbnail has created: {folder_ubication_thumb}")
		else:
			print(f"Folder thumbnail already exists: {folder_ubication_thumb}")


	#__ Método para obtener un "frame" del video  __#
	def make_thumbnail(self, folder_ubication, filename, frame_at_seconds = 100):
		clip = VideoFileClip(folder_ubication + f"/{filename}")
		frame_at_seconds = frame_at_seconds
		frame = clip.get_frame(frame_at_seconds)

		return frame


	#__ Convertimos un verctor Numpy en una imagen __#
	def make_thumbnail_image(self, image_array):
		return Image.fromarray(image_array)


	#__ Método para redimensionar la imagen __#
	def resize_image(self, obj_image, width, height):
		return obj_image.resize((width, height))
			

	#__ Guardamos la imagen en la ubicación preferida __#
	def save_image(self, obj_image, folder_ubication, filename):
		obj_image.save(folder_ubication + f"/{filename[:-4]}.jpg", quality = 95)
		return f"Image has Saved: {filename}"


	#__ Guardamos la imagen en la ubicación preferida __#
	def is_thumb_exist(self, file_thumb):
		return os.path.exists(f'{file_thumb[:-4]}.jpg')