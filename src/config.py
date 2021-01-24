from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask, config


app = Flask(__name__)
app.secret_key = "randomstring"
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

