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
	def __init__(self):
		self.URL_VIDEO = "/home/yilver/Videos"
		self.URL_THUMBNAILS = os.getcwd() + "static/img/thumbnails"


	#__ Método para crear carpetas __#
	def make_folder(self, folder_name, folder_ubication):
		folder_create = folder_ubication + f"/{folder_name}"
		create_folder = os.makedirs(folder_create, exist_ok = True)
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



#################################################
#####Obtener Una Lista de Archivos###############
#################################################
def get_list_items(folder_ubication):
	just_files = []
	list_files = os.listdir(folder_ubication)
	for item in list_files:
		if os.path.isfile(folder_ubication + f"/{item}"):
			just_files.append(item)

	return just_files

#################################################
#########Ejecutamos la aplicación################
#################################################
if __name__ == '__main__':
	pass 

	"""
	#create thumbnail_folder
	#-----------------------
	lista = ["Temporada 1",
			 "Temporada 2",
			 "Temporada 3"]
	for i in lista:
		URL_FOLDER = os.getcwd() + "/static/img/thumbnails"
		thumbnail = Thumbnails()

		folder_ubication = URL_FOLDER + "/thumbnails_comiquitas/thumbnails_el_increible_mundo_de_gumball"
		folder_name = f"thumbnails_{i.replace(' ', '_').lower()}"
		
		create_folder = thumbnail.make_folder(folder_name, folder_ubication)
	"""

	#create thumbnail_file_img
	#-----------------------
	lista_thu = ["thumbnails_temporada_1",
				 "thumbnails_temporada_2"]

	lista = ["Temporada 1",
			 "Temporada 2"]
	thumbnail = Thumbnails()
	for j in range(len(lista)):
		Global_FOLDER = "/home/yilver/Videos" + "/Comiquitas/El Increible Mundo De Gumball/" + lista[j]
		folder_ubication = os.getcwd() + "/static/img/thumbnails/thumbnails_comiquitas/thumbnails_el_increible_mundo_de_gumball/" + lista_thu[j] 
		files = get_list_items(Global_FOLDER)
		for i in files:
			image_thumbnail = thumbnail.make_thumbnail(i, Global_FOLDER)
			image 	= thumbnail.make_thumbnail_image(image_thumbnail)
			image 	= thumbnail.resize_image(image, width = 350, height = 200)
			message = thumbnail.save_image(image, folder_ubication, i)
			print(message)
	
