#python comunicación con la base de datos

import os

videos_route = "/home/yilver/Videos"


#remover contenido no deseado
def remove_items(tags_list):
	print(tags_list)
	for tag in tags_list:
		if tag[0] == "_": #El contenido no deseado tendrá un _ en la posición 0
			tags_list.remove(tag)
			
	for tag in tags_list:
		if tag[0] == "_": #El contenido no deseado tendrá un _ en la posición 0
			tags_list.remove(tag)

	print(tags_list)
	return tags_list


#Obtener las carpetas que esten en la carpeta Videos o videos_route
def get_tags():
	tags_list = os.listdir(videos_route)
	return remove_items(tags_list)


#Obtener los items o videos que esten en una carpeta
def get_all_items(folder, videos_route = videos_route):
	is_folder = {}
	tags_list = os.listdir(videos_route + f"/{folder}")
	tags_list = remove_items(tags_list)
	for i in tags_list:
		if i.find(".") != -1:
			is_folder[i] = False
		else: 
			is_folder[i] = True
	return is_folder


if __name__ == '__main__':
	print(get_tag_items())