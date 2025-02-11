import os.path
import secrets

from PIL import Image
from flask import current_app


def save_picture(pic):
    if pic:
        random_hex = secrets.token_hex(8)
        _, ext = os.path.splitext(pic.filename)
        pic_name = random_hex + ext
        picture_path = os.path.join(current_app.config['SERVER_PATH'], pic_name)
        output_size = (125, 125)
        i = Image.open(pic)
        i.thumbnail(output_size)
        i.save(picture_path)
        return pic_name
    return ''

def recursive_flatten_iterator(d):
    pass