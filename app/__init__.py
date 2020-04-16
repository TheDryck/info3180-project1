from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI ='postgres://wwqzkthoioobwg:74780fba2df748e06bc34716544df6364d9c2ef1a7601bbf671d9bfa244b6e2c@ec2-34-193-232-231.compute-1.amazonaws.com:5432/dc40f7bs7m34l8'
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = "./app/static/uploads"
SECRET_KEY = '1234567890'

app.config.from_object(__name__)

db = SQLAlchemy(app)

from app import views