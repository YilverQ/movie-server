"""
	Variales. 
	------------------------------------
	Flask = Es una clase de tipo Flask. Nos crea una aplicación de Flask. 
	Config = Tiene los parámetros de configuración. 
	global_scope = Tiene las URL. 

	¿Qué hace el código?
	------------------------------------
	Creamos una aplicación Flask.
	Le pasamos los parámatros de configuración para los archivos estáticos (Imágenes)
	Le pasamos los parámatros de configuración para los archivos HTML.
	A nuestra aplicación 'app' le pasamos un objeto de configuración. 
	Registramos el blueprint (global_scope) a nuestra aplicación.
"""
from flask import Flask
from config import Config
from .routes import global_scope

app = Flask(__name__, 
			static_folder = Config.STATIC_FOLDER,
			template_folder = Config.TEMPLATE_FOLDER)
app.config.from_object(Config)

app.register_blueprint(global_scope, url_prefix = '/')