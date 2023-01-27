"""
	Esta es una forma alternativa de iniciar
	la aplicación, para ello usar: 

		python -m app

	Estando en la carpeta raíz.
"""

from . import app
from .thumbnails import *

if __name__ == '__main__':
	make_thumbnails()
	app.run()