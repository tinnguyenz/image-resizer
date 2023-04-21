import os
from io import BytesIO
import base64

from flask import Flask, request, jsonify
from PIL import Image

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/api/v1/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']

    try:
        img = Image.open(file.stream)
    except:
        return jsonify({'error': 'Invalid image file'}), 400

    img.thumbnail((200, 200))

    thumb_io = BytesIO()
    img.save(thumb_io, 'JPEG')
    thumb_io.seek(0)

    save_path = os.path.join('/app/images', 'thumbnail.jpg')
    with open(save_path, 'wb') as f:
        f.write(thumb_io.getvalue())

    data_url = f"data:image/jpeg;base64,{base64.b64encode(thumb_io.getvalue()).decode()}"

    return jsonify({'thumbnail': data_url}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
