import telebot

from telebot import types

bot = telebot.TeleBot("1058610099:AAEj7aFjSgtU5ZbO4_cwanWKlYw-gxsNRLI")


def construct_message_text(post):
    return f'**{post["title"]}**\n\n\n{post["excerpt"]}\n\n{post["url"]}\n\n Kanalimizga obuna bo\'ling!!! '


def notify_by_telegram_channel(post):
    chat_id = "-1001446422523"# CHANNEL ID
    # txt = order_details_text(order)
    txt = construct_message_text(post)
    bot.send_message(chat_id=chat_id, text=txt, parse_mode='Markdown')

