import os
from dotenv import load_dotenv

load_dotenv()

db_path = os.path.join(os.path.dirname(__file__), 'site.db')
db_uri = 'sqlite:///{}'.format(db_path)


class Config:
    APP_NAME = os.environ.get('APP_NAME')
    APP_URL = os.environ.get('APP_URL')
    DEBUG_MODE = os.environ.get('DEBUG_MODE')
    # Database
    SQLALCHEMY_DATABASE_URI = db_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS')

    CELERY_BROKER_URL = ""

    DB_CONNECTION_URL = os.environ.get('DB_CONNECTION_URL')

    GHOST_CC_TOKEN = os.environ.get('GHOST_CC_TOKEN')

    FB_GRAPH_API_TOKEN = os.environ.get('FB_GRAPH_API_TOKEN')

    TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

    FB_PAGE_ID = os.environ.get('FB_PAGE_ID')
    TELEGRAM_CHANNEL_CHAT_ID = os.environ.get('TELEGRAM_CHANNEL_CHAT_ID')
