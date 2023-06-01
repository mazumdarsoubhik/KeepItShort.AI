from instagrapi import Client
# from instagrapi.types import Usertag
import configparser

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

cl = Client()
cl.login(config['instagram']['username'], config['instagram']['password'])

def post_image(url, caption):
    try:
        media = cl.photo_upload(
            path=f"{url}",
            caption=f"{caption}"
        )
        return 200
    except:
        return 400

if __name__ == '__main__':
    # read configs
    config = configparser.ConfigParser()
    config.read('../config.ini')

    cl = Client()
    cl.login(config['instagram']['username'], config['instagram']['password'])

    media = cl.photo_upload(
        path="../kisai.jpeg",
        caption="My first post via API..."
    )