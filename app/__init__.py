from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# SQLALCHEMY_DATABASE_URI ="postgresql://project1:jordan@localhost/project1"
SQLALCHEMY_DATABASE_URI ="postgresql://yecsapnzlttgcb:8860d3512549e3ebba04aa68ede74496e30041ff458ea1d46d7c4ed7f5402af0@ec2-54-221-244-196.compute-1.amazonaws.com:5432/d9d6gbbcjoc71g"
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = "./app/static/uploads"
SECRET_KEY = '1234567890'

app.config.from_object(__name__)

db = SQLAlchemy(app)

from app import views