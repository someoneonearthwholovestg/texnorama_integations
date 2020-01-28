from dotenv import load_dotenv


load_dotenv()


import os

APP_NAME = os.getenv("APP_NAME")
APP_URL = os.getenv("APP_URL")

DB_CONNECTION_URL = os.getenv("DB_CONNECTION_URL")

GHOST_CC_TOKEN = os.getenv("GHOST_CC_TOKEN")
FB_GRAPH_API_TOKEN = os.getenv("FB_GRAPH_API_TOKEN")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

FB_PAGE_ID = os.getenv("FB_PAGE_ID")
CHAT_ID = os.getenv("CHAT_ID")
