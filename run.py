from app import app
from app.thumbnails import init_thumbnails
from app.helpers import init_folders_videos

if __name__ == '__main__':
    init_folders_videos()
    init_thumbnails()
    app.run()