import os


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
from config import Config
import facebook
import telebot

db = SQLAlchemy()
# celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)
graph = facebook.GraphAPI(access_token=Config.FB_GRAPH_API_TOKEN)
bot = telebot.TeleBot(Config.TELEGRAM_BOT_TOKEN)


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # app.config
    app.config.from_object('config.Config')
    
    db.init_app(app)

    # celery.conf.update(app.config)

    with app.app_context():
        from . import routes

        db.create_all()

        return app
