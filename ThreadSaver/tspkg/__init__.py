from flask import Flask
from flask_dance.contrib.twitter import make_twitter_blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dude280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../../site.db'

twitter_bp = make_twitter_blueprint(api_key='api key here', api_secret='api secret key here')  # main account api
app.register_blueprint(twitter_bp, url_prefix="/login")

db = SQLAlchemy(app)

from tspkg import routes
