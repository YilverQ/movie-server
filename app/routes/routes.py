"""
	Variables
	------------------------------------
	Blueprint = Se utiliza para crear rutas y luego anexarlas a la aplicación. 
	render_template = Nos retorna un archivo HTML. (Podemos pasarle parámetros).
	send_from_directory = Nos retorna un archivo para ser descargado. 
	global_scrope = Sirve para agregar rutas nuevas. 
	nav = Contiene las etiquetas principales de la aplicación.
	parameters = Contiene los atributos para el HTML.
"""

from flask import Blueprint, render_template, send_from_directory
from ..database.Folder_db import Folder_DB
from ..helpers.helper import format_url, get_title, transform_text
from config import Config
global_scope = Blueprint('views', __name__)
db = Folder_DB()


@global_scope.route('/')
def index():
	parameters = {'title' 	: 'Home',
				  'tags' 	: db.get_folders()}

	return render_template("index.html", **parameters)


@global_scope.route('/folder/<string:element>')
def folder(element):
	element 	= format_url(element)
	parameters 	= {'title' 	: element,
				  'tags' 	: db.get_folders(),
				  'folders' : db.get_folders(element),
				  'files' 	: db.get_files(element),
				  'location': element,
				  'adress'	: Config.SERVER_NAME}
	
	return render_template("item.html", **parameters)


@global_scope.route('/download_video/<string:folder>/<string:item_download>')
def download_video(folder, item_download):
	item_download = format_url(item_download)
	folder = Config.VIDEO_FOLDER + format_url(folder) + "/"
	return send_from_directory(folder, item_download)