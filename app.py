from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   # a warning msg doesn't appear when we run app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'   # the location of database

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.now)

