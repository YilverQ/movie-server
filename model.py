"""
	Modelo: Los datos de la página los saca en las carpetas del OS.
"""

import os

class MovieServer:
	def __init__(self):
		self.folder_tags = "/home/yilver/Videos"
		self.folder = "/home/yilver/Videos"
		

	def get_tags(self):
		contenido = os.listdir(self.folder_tags)
		tags_list = []
		for tag in contenido:
			if not (tag[0] == "_" or "." in tag):
				tags_list.append(tag)
		return tags_list


	def get_items_folder(self):
		items_list 	= []
		for item in os.listdir(self.folder):
			if not(item[0] == "_" or "." in item):
				items_list.append(item)
		items_list.sort()
		return items_list


	def get_items_videos(self):
		items_list = []
		for item in os.listdir(self.folder):
			if (item[0] != "_") and ("." in item):
				items_list.append(item)
		items_list.sort()
		return items_list


if __name__ == '__main__':
	obj = MovieServer()
	obj.folder = "/home/yilver/Videos/Películas"
	print(obj.get_items_in_folder())
	obj.folder = "/home/yilver/Videos/Series"
	print(obj.get_items_in_folder())
	obj.folder = "/home/yilver/Videos/Animes"
	print(obj.get_items_in_folder())