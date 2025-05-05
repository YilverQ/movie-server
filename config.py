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
import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SERVER_NAME = os.getenv('SERVER_NAME')  
    DEBUG = os.getenv('DEBUG', 'False') == 'True'  

    TEMPLATE_FOLDER = 'views/templates/'
    STATIC_FOLDER = 'views/static/'
    VIDEO_FOLDER = os.getenv('VIDEO_FOLDER')
    FOLDER_THUMBNAILS=os.path.join(os.getcwd(), 'app/views/static/img/thumbnails/')