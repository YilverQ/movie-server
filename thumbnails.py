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


def _check_thumbnail(folder_ubication, thumbnail_file):
	pass

#################################################
#########Ejecutamos la aplicación################
#################################################
if __name__ == '__main__':
	pass 

	"""
	#create thumbnail_folder
	#-----------------------
	URL_FOLDER = os.getcwd() + "/static/img/thumbnails"
	thumbnail = Thumbnails()

	folder_ubication = URL_FOLDER + "/thumbnails_series"
	folder_name = f"thumbnails_{'The Good  Doctor 4'.lower()}"
	
	create_folder = thumbnail.make_folder(folder_name, folder_ubication)
	"""
	

	
	#create thumbnail_file_img
	#-----------------------
	thumbnail = Thumbnails()
	Global_FOLDER = "/home/yilver/Videos" + "/Series/Ted Lasso T2"
	folder_ubication = os.getcwd() + "/static/img/thumbnails/thumbnails_series/thumbnails_ted lasso t2" 
	files = get_list_items(Global_FOLDER)
	for i in files:
		image_thumbnail = thumbnail.make_thumbnail(i, Global_FOLDER)
		image 	= thumbnail.make_thumbnail_image(image_thumbnail)
		image 	= thumbnail.resize_image(image, width = 100, height = 80)
		message = thumbnail.save_image(image, folder_ubication, i)
		print(message)
	

	"""
	#check thumbnail_file
	URL_FOLDER = os.getcwd() + "/static/img/thumbnails"
	folder_ubication = URL_FOLDER + "/thumbnails_películas"
	folder_videos = "/home/yilver/Videos/Películas"
	files = get_list_items(folder_videos)
	files_thumbnails = get_list_items(folder_ubication)
	lista = []
	for i in files:
		if not (i[:-4]+".jpg" in files_thumbnails):
			lista.append(i)
	print(f"archivos sin thumbnails: \n {lista}")
	"""
