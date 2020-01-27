import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from telebot import types
from setting import TELEGRAM_BOT_TOKEN, CHAT_ID

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


def construct_message_text(post):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton('Link', url = post['url'])
    markup.add(btn)
    # return [f'**{post["title"]}**\n\n\n{post["excerpt"]}\n\n{post["url"]}\n\n Kanalimizga obuna bo\'ling!!! ', markup]
    return [f"""
    <strong>{post["title"]}</strong>
    {post["excerpt"]}
    <a href=\"{post["url"]}\"> </a>
    Kanalimizga obuna bo'ling!!!
    """, markup]


def notify_by_telegram_channel(post):
    chat_id = CHAT_ID# CHANNEL ID
    # txt = order_details_text(order)
    txt, markup = construct_message_text(post)
    msg = bot.send_message(chat_id=chat_id, text=txt, parse_mode='HTML', reply_markup=markup)
    return msg.message_id

def  edit_message_text(post, msg_id):
    chat_id = CHAT_ID# CHANNEL ID
    txt, markup = construct_message_text(post)
    bot. edit_message_text(message_id=msg_id,  chat_id=chat_id, text=txt, parse_mode='HTML', reply_markup=markup)
    return "cool"


