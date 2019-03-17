from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI ="postgresql://project1:jordan@localhost/project1"
# SQLALCHEMY_DATABASE_URI ='postgresql ://zgtoxumhngmani:0558ab5b22a98a4dc2abc7a5d61fe8b96bf432a5f0a974879963d2b3b34103b8@ec2-107-20-177-161.compute-1.amazonaws.com:5432/d38m9t7hnj4t7m'
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = "./app/static/uploads"
SECRET_KEY = '1234567890'

app.config.from_object(__name__)

db = SQLAlchemy(app)

from app import views