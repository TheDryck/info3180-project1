from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI ='postgres://kxjwalihfmxypq:2e6a6f6500e434ba75c8a672f72d47d67113e47bbe508fc5302b48f70b5b2980@ec2-75-101-133-29.compute-1.amazonaws.com:5432/dbl55tm7qr4blt'
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = "./app/static/uploads"
SECRET_KEY = '1234567890'

app.config.from_object(__name__)

db = SQLAlchemy(app)

from app import views