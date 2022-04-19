from flask import Flask, render_template, send_from_directory
from model import *


app = Flask(__name__)
carpeta_madre = "get_items_in_folder"
objeto = MovieServer()
diccionario = {	"title" : "", "tags" : "", "URL_FOLDER":"", "item_folder" : "", "item_videos":""}


@app.route("/")
def index():
	diccionario["title"] = "Home"
	diccionario["tags"] = objeto.get_tags()
	return render_template("index.html", datos = diccionario)


@app.route("/folder/<string:folder>")
def tag_main(folder):
	objeto.folder = objeto.folder_tags + "/" + folder.replace("-", " ").replace("&", "/")
	diccionario["URL_FOLDER"] = folder.replace("/", "&")
	diccionario["title"] = objeto.folder[objeto.folder.rfind("/")+1:]
	diccionario["tags"] = objeto.get_tags()
	diccionario["item_folder"] = objeto.get_items_folder()
	diccionario["item_videos"] = objeto.get_items_videos()
	return render_template("item.html", datos = diccionario)


@app.route("/download_video/<string:folder>/<string:item_download>")
def download_video(folder, item_download):
	folder = "/home/yilver/Videos/" + folder.replace('&', '/').replace('-', " ") + "/"
	item_download = item_download.replace('&', '/').replace('-', " ")
	return send_from_directory(folder, item_download)


@app.route("/video_online/<string:folder>/<string:item_download>")
def video_online(folder, item_download):
	video = {}
	folder = "/home/yilver/Videos/" + folder.replace('&', '/').replace('-', " ") + "/"
	item_download = item_download.replace('&', '/').replace('-', " ")
	diccionario["title"] = item_download[:-4]
	diccionario["tags"] = objeto.get_tags()
	video["folder"] = folder
	video["item_download"] = item_download
	return render_template("online.html", datos = diccionario, video = video)


if __name__ == '__main__':
	app.run(debug = True,  port = 5000)

#host = 192.168.43.7
