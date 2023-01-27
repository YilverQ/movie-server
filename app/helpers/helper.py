#Script para formatear las rutas. 

"""
	Diccionario:

		& = son /
		- : son espacios en blancos.
"""

def format_url(string):
	string = string.replace("-", " ")
	string = string.replace("&", "/")
	return string


def get_title(string):
	return string[string.rfind("/")+1:]


def transform_text(string):
	string = string.replace(" ", "-")
	string = string.replace("/", "&")
	return string