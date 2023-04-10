"""
	Clase: Config
	--------------------------------------------------
	SERVER_NAME = Tiene la dirección IP de nuestro dispositivo. 
	PORT = El puerto por el cual se ejecutará.
	DEBUG = Indicamos si estamos en modo desarrollador. 

	TEMPLAE_FOLDER = Ubicación de los archivos HTML.
	STATIC_FOLDER = Ubicación de los archivos media (Imágenes, etc).
	VIDEO_FOLDER = Ubicación de nuestros vídeos. 
	FOLDER_THUMBNAILS = Ubicación dónde estarán las miniaturas de los vídeos.
"""

class Config:
	SERVER_NAME = '192.168.2.112:5000'
	DEBUG = True

	TEMPLATE_FOLDER = 'views/templates/'
	STATIC_FOLDER 	= 'views/static/'
	VIDEO_FOLDER 	= '/home/canaima/Vídeos/'
	FOLDER_THUMBNAILS = '/app/views/static/img/thumbnails/'