# flask_s3_uploads/config.py

import os

S3_BUCKET = os.environ.get("S3_BUCKET_NAME")
S3_KEY = os.environ.get("S3_ACCESS_KEY")
S3_SECRET = os.environ.get("S3_SECRET_ACCESS_KEY")
S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

SECRET_KEY = os.urandom(32)
DEBUG = True
PORT = 5000

UPLOAD_FOLDER = '/Users/kevin/WaveWatch/wave-watch-server/uploads'
DATABASE = '/users/kevin/WaveWatch/wave-watch-server/database.db'
