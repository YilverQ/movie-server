from .make_thumbnails import make_thumbnails
from .make_folders_thumbs import make_folders_thumbs

def init_thumbnails():
    make_folders_thumbs()
    print()
    make_thumbnails()