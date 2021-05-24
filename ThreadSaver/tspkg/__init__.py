from os import environ

from flask import Flask
from flask_dance.contrib.twitter import make_twitter_blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dude280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../site.db'

Consumer_key_web = environ['Consumer_key_web']
Consumer_key_secret_web = environ['Consumer_key_secret_web']
twitter_bp = make_twitter_blueprint(Consumer_key_web, Consumer_key_secret_web)  # main account api
app.register_blueprint(twitter_bp, url_prefix="/login")

db = SQLAlchemy(app)

from tspkg import routes
