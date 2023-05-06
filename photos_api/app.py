import os
from io import BytesIO
import base64

from flask import Flask, request, jsonify
from PIL import Image
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

"""
db_conn = os.environ.get("DATABASE_URL")
if not db_conn:
    db_conn = "postgresql://postgres:postgres@db:5432/photos"
conn = psycopg2.connect(db_conn)
"""

def connect_db():
    conn = psycopg2.connect(
        host='db',
        user='postgres',
        password='postgres',
        dbname='photos'
    )
    return conn

class Photo:
    def __init__(self, id, image):
        self.id = id
        self.image = image

    def to_dict(self):
        return {"id": self.id}

    @staticmethod
    def from_dict(photo_dict):
        return Photo(photo_dict["id"], photo_dict["image"])

    @staticmethod
    def create(image):
        with conn, conn.cursor() as cur:
            cur.execute(
                "INSERT INTO photos (image) VALUES (%s) RETURNING id", (image,)
            )
            id = cur.fetchone()[0]
        return Photo(id, image)

    @staticmethod
    def get(id):
        with conn, conn.cursor() as cur:
            cur.execute("SELECT * FROM photos WHERE id = %s", (id,))
            row = cur.fetchone()
        if row is None:
            return None
        return Photo(row[0], row[1])


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

    """
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO photos (resized_image) VALUES (%s) RETURNING id", 
        [psycopg2.Binary(thumb_io.getvalue())]
    )
    id = cursor.fetchone()[0]

    conn.commit()
    cursor.close()
    conn.close()
    """

    save_path = os.path.join('/app/images', 'thumbnail.jpg')
    with open(save_path, 'wb') as f:
        f.write(thumb_io.getvalue())

    data_url = f"data:image/jpeg;base64,{base64.b64encode(thumb_io.getvalue()).decode()}"

    return jsonify({'thumbnail': data_url}), 200
    #return jsonify({'id': id}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
