from flask import Flask, render_template, request, jsonify
import os
import base64
import random
from helpers import file_upload


app = Flask(__name__)


IMAGE_DIR = 'uploaded_images'
os.makedirs(IMAGE_DIR, exist_ok=True)


import routes


@app.post('/upload')
def upload():
    base64_string = request.json['image']
    image_path = os.path.join(IMAGE_DIR)
    name = random.randint(1, 1000)
    name = f"{name}uploaded_image.png"
    file = file_upload.upload(base64_string, image_path, name)
    return file


if __name__ == '__main__':
    app.run()
