import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from telebot import types
from settings import TELEGRAM_BOT_TOKEN, CHAT_ID

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


def construct_message_text(post):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton('Batafsil', url=post['url'])
    markup.add(btn)
    # return [f'**{post["title"]}**\n\n\n{post["excerpt"]}\n\n{post["url"]}\n\n Kanalimizga obuna bo\'ling!!! ', markup]
    return [f"""
    {post["title"]}

Kanalimizga obuna bo'ling!!!
https://t.me/texnorama
    """, markup]


def notify_by_telegram_channel(post):
    chat_id = CHAT_ID# CHANNEL ID
    print(f'========CHAT_ID = {chat_id}===============')
    # txt = order_details_text(order)
    txt, markup = construct_message_text(post)
    try:
        # msg = bot.send_message(chat_id=chat_id, text=txt, parse_mode='HTML', reply_markup=markup)
        msg = bot.send_photo(chat_id=chat_id, photo=post['feature_image'], caption=txt, reply_markup=markup)
        return msg.message_id
    except Exception as e:
        print(e)
        return None


def edit_message_text(post, msg_id):
    chat_id = CHAT_ID# CHANNEL ID
    txt, markup = construct_message_text(post)
    try:
        bot.edit_message_text(message_id=msg_id,  chat_id=chat_id, text=txt, parse_mode='HTML', reply_markup=markup)
    except Exception as e:
        print(e)
    return "cool"


