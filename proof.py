"""
	Este archivo no es para ejecutarse, es para poner bloques de código como ejemplos. 
"""



#prueba para obtener un thumbdails de un video con la ayuda de python y un paquete de ffvideo

#import subprocess

url = "/home/yilver/Documentos/proyects/movie_server/"

video_input = (url + "stone.mp4")

img_output = url + "capturas/"

time =  ["00:00:50.000", "00:01:30.000", "00:05:00.000",
		 "00:07:00.000", "00:09:00.000", "00:10:00.000",
		 "00:12:00.000", "00:18:00.000", "00:20:00.000",
		 "00:21:00.000"]

for i in range(10):
	subprocess.call(["ffmpeg", "-i", video_input, "-ss", time[i], "-vframes", "1", (img_output + f"image{i}.jpg")])


"""

import os 
import subprocess
from model import *


url_videos = "/home/yilver/Videos"
url_thumbnails = os.getcwd() + "/static/img/thumbnails"


def make_folder():
	tag_list = get_tags()
	change = os.chdir(url_thumbnails)
	for i in tag_list:
		folder =  os.makedirs(f"thumbnails_{i.lower()}")
		print(f"thumbnails_{i.lower()} \n Ha Sido Creado Exitosamente \n")

	return "El Proceso Ha Finalizado"


def make_thumbnails_movies(tag = "Películas"):
	time = "00:03:30.000"
	images_input = get_tag_items()
	images_output = url_thumbnails + f"/thumbnails_{tag.lower()}/"
	url_converter = url_videos + "/" + tag + "/"
	for image in images_input:
		if image[0] != "_":
			text_title = image[:-4].replace(" ", "_").lower()
			subprocess.call(["ffmpeg", "-i", (url_converter + image), 
							 "-ss", time, "-vframes", "1", 
							 (images_output + f"{text_title}.jpg")])

			print(f"{image} \nHa Sido Creado Exitosamente!!! :D \n")

	return "El Proceso Ha Finalizado"
	

if __name__ == '__main__':
	print(make_thumbnails_movies())

"""

from moviepy.editor import *

#Configuración de las URLs
URL_VIDEO = "/home/yilver/Documentos/proyects/movie_server"
URL_THUMBNAILS = os.getcwd() + "/static/img/thumbnails"


#ejemplo de como trabajarlo
clip =  VideoFileClip(URL_VIDEO + "/sample.mp4") #Objeto
#nframes_seconds = clip.reader.fps #retorna el numero de frames por segundos
nframes_video = clip.reader.nframes #retorna el numero de frames del video
duration = clip.duration #devuelve cuanto dura el video en segundos
max_duration = int(clip.duration) + 1

frame_at_seconds = 28 #aquí es el timepo cuando realizara el thumbnail en segundo
frame = clip.get_frame(frame_at_seconds) #obtiene un nympy array representado en RGB

new_image_filepath = URL_THUMBNAILS + "/thumbnails_películas"
new_image = Image.fromarray(frame) #convierte el array en una imagen
new_image.save(new_image_filepath + "example.jpg") #guardamos la imagen


#"""
"""
	Make Folder
	Make Thumbnails
"""






"""
#Variables Globales
URL_VIDEO = "/home/yilver"
URL_THUMBNAILS = os.getcwd() + "/static/img/thumbnails"
URL_VIDEO_COPY = URL_VIDEO + "/Videos"
URL_THUMBNAILS_COPY = URL_THUMBNAILS

#Crear Carpetas Para los Thumbnails

#Restablecer las Variables que comienzan con URL
def restar_URLs(ubication = ""):
	global URL_VIDEO, URL_THUMBNAILS
	if ubication != "":
		URL_VIDEO = URL_VIDEO_COPY + "/" + ubication
		URL_THUMBNAILS = URL_THUMBNAILS_COPY + "/thumbnails_" + ubication.lower()
	else: 
		URL_VIDEO = URL_VIDEO_COPY
		URL_THUMBNAILS = URL_THUMBNAILS_COPY
	return 1


#Crea las carpetas thumbnails
def make_folder(folder, first = False):
	global URL_VIDEO, URL_THUMBNAILS
	items_list = get_all_items(folder, videos_route = URL_VIDEO)
	name_folder = "thumbnails_"


	#Cambiar a Directorio
	if first == True:
		change_folder = os.chdir(URL_THUMBNAILS)
	else:
		change_folder = os.chdir(URL_THUMBNAILS + f"/{name_folder}{folder.lower()}")
		URL_THUMBNAILS = URL_THUMBNAILS + f"/{name_folder}{folder.lower()}"


	#Para Crear las carpetas
	for key, value in items_list.items():
		name_folder = f"thumbnails_{key.lower()}"
		if value:
			create_folder = os.makedirs(name_folder, exist_ok = True)
			print(f"{name_folder} \n Ha Sido Creado Exitosamente \n")


	URL_VIDEO = URL_VIDEO + "/" + folder
	return 1


#Esta es la funcion principla para crear la carpeta, es una prueba
def fuction_make_folder():
	var = make_folder("Videos", True)
	
	#Iteramos las carpetas que están en Videos
	for i in ["Animes", "Películas", "Series"]:
		var = make_folder(i)
		
		#Listamos los elementos de las carpetas para crear thumbnails en caso de que hayan subcarpetas
		items_list = get_all_items(i)
		for key, value in items_list.items():
			if key.find(".") == -1:
				var = make_folder(key)
				var = restar_URLs(i)
		
		var = restar_URLs()


def get_thumbnails(folder, other_folder):
	global URL_VIDEO, URL_THUMBNAILS
	restar = restar_URLs()
	name_folder = "thumbnails_"

	#cambiar a directorio de trabajo
	chage_folder_thumbnails = os.chdir(URL_THUMBNAILS + f"/{name_folder}{folder.lower()}/{name_folder}{other_folder.lower()}")
	URL_THUMBNAILS = URL_THUMBNAILS + f"/{name_folder}{folder.lower()}/{name_folder}{other_folder.lower()}"
	chage_folder_videos = os.chdir(URL_VIDEO + "/" + folder + "/" + other_folder)
	URL_VIDEO = URL_VIDEO + "/" + folder + "/" + other_folder

	print(f"---URL_VIDEO---\n{URL_VIDEO}")
	print(f"---URL_THUMBNAILS---\n{URL_THUMBNAILS}")

	#para crear los thumbnails
	print(URL_VIDEO[:URL_VIDEO.rfind("/")])
	item_list = get_all_items(folder = other_folder, videos_route = URL_VIDEO[:URL_VIDEO.rfind("/")])
	for key, value in item_list.items():
		if folder_exist():
			if value != True:
				clip = VideoFileClip(URL_VIDEO + "/" + key)
				frame_at_seconds = 100
				frame = clip.get_frame(frame_at_seconds)

				path_image = URL_THUMBNAILS
				new_image = Image.fromarray(frame)
				new_image = new_image.resize((120,80))
				new_image.save(path_image + f"/{key[:-4]}.jpg", quality = 95)
				print(f"{key[:-4]} Ha Sido Creado El thumbnails en")
				print(path_image + f"/{key[:-4]}.jpg\n")

	return "Finished"


if __name__ == '__main__':
	#print(get_thumbnails("Series","vikings T5"))
	#print(get_thumbnails("Animes", "Boku No Hero T5"))
	#print(get_thumbnails("Animes", "Dr Stone T2"))
	#print(get_thumbnails("Películas", "Películas Vistas"))
	######################################################

	print(get_thumbnails("Series","Deadly Class"))
	print(make_folder)


"""
	Hacer que elija solamente cuando estemos en la carpeta destino
	osea, hacer que la función make_folder solamente trabaje para hacer carpetas
	y crear otra carpeta para realizar saltos entre carpetas
"""

"""


#create thumbnail_folder
	#-----------------------
	URL_FOLDER = os.getcwd() + "/static/img/thumbnails"
	thumbnail = Thumbnails()

	folder_ubication = URL_FOLDER + "/thumbnails_series"
	folder_name = f"thumbnails_{'Deadly Class'.lower()}"
	
	create_folder = thumbnail.make_folder(folder_name, folder_ubication)


	#create thumbnail_file_img
	#-----------------------
	Global_FOLDER = "/home/yilver/Videos" + "/Series/Deadly Class"
	folder_ubication = os.getcwd() + "/static/img/thumbnails/thumbnails_series/thumbnails_deadly class" 
	files = get_list_items(Global_FOLDER)
	files = remove_folders(files)
	for i in files:
		image_thumbnail = thumbnail.make_thumbnail(i, Global_FOLDER)
		image 	= thumbnail.make_thumbnail_image(image_thumbnail)
		image 	= thumbnail.resize_image(image, width = 100, height = 80)
		message = thumbnail.save_image(image, folder_ubication, i)
		print(message)
