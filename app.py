from flask import Flask, render_template, send_from_directory
from model import *


app = Flask(__name__)
URL_FOLDER = "/home/yilver/Videos"
diccionario = {	"title" : "", "tags" : "", "item_in_folder" : "", "folder_father" : "", 
				"URL_Download" : ""}
app.config["UPLOAD_FOLDER"] = URL_FOLDER

@app.route("/")
def index():
	diccionario["title"] = "Home"
	diccionario["tags"] = get_tags()
	return render_template("index.html", datos = diccionario)


@app.route("/tag/<string:item>")
def tag_main(item):
	diccionario["title"] = item
	diccionario["tags"] = get_tags()
	diccionario["folder_father"] = item
	diccionario["item_in_folder"] = get_all_items(item)
	diccionario["URL_Download"] = URL_FOLDER + f"/{item}"
	return render_template("item.html", datos = diccionario)


@app.route("/tag_folder/<string:folder>/<string:item>")
def folder(folder, item):
	diccionario["title"] = item
	diccionario["tags"] = get_tags()
	diccionario["item_in_folder"] = get_all_items(item, URL_FOLDER + f"/{folder}")
	diccionario["folder_father"] = folder + "/thumbnails_" + item.lower()
	diccionario["URL_Download"] = URL_FOLDER + f"/{folder}/{item}/"
	#diccionario["Videos_Route"] = URL_FOLDER + f"/{folder}"
	return render_template("item.html", datos = diccionario)


@app.route("/download_video/<string:url>/<string:item_download>")
def download_video(item_download, url):
	#return f"VIDEO_FOLDER = {url.replace('!', '/')}<br> ITEM_NAME = {item_download.replace('!', '/')}"
	return send_from_directory(url.replace('!', '/'), item_download.replace('!', '/'))


@app.route("/video_online/<string:url>/<string:item_download>")
def video_online(item_download, url):
	video = {}
	diccionario["title"] = item_download
	diccionario["tags"] = get_tags()
	video["url"] = url
	video["item_download"] = item_download
	return render_template("video.html", datos = diccionario, video = video)


if __name__ == '__main__':
	app.run(debug = True, port = 5000)

#host = 192.168.43.7
