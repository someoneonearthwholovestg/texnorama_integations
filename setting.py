from dotenv import load_dotenv


load_dotenv()


import os

APP_NAME = os.getenv("APP_NAME")
APP_URL = os.getenv("APP_URL")

DB_CONNECTION_URL = os.getenv("DB_CONNECTION_URL")

GHOST_CC_TOKEN = os.getenv("GHOST_CC_TOKEN")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

CHAT_ID = os.getenv("CHAT_ID")
