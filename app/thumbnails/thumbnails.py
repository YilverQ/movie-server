"""
	Hacer Thumbnails con Python 3, usando el modulo de moviepy y Pillow (PIL)

"""

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
	def make_folder(self, folder_name, folder_ubication):
		route = folder_ubication
		route += f"/{folder_name}"
		create_folder = os.makedirs(route, exist_ok = True)
		return f"{folder_name}, Folder has Created!"


	#__ Método para obtener un "frame" del video  __#
	def make_thumbnail(self, filename, folder_ubication, frame_at_seconds = 100):
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
		return f"{filename}, Image has Saved!!!"