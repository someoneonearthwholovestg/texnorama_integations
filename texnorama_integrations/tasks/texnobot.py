import traceback

import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

from telebot import types
# from settings import TELEGRAM_BOT_TOKEN, CHAT_ID


from . import pub_service
from .. import bot, Config

import sys
import pathlib
project_path = pathlib.Path(__file__).parents[2]
sys.path.insert(0, str(project_path))
from logger import get_logger


logger = get_logger()

@logger.catch
def construct_message_text(post):
    logger.info("\n============ Message is Constructed from Post <slug: {}>==================".format(post['slug']))
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton('Batafsil', url=post['url'])
    markup.add(btn)
    # return [f'**{post["title"]}**\n\n\n{post["excerpt"]}\n\n{post["url"]}\n\n Kanalimizga obuna bo\'ling!!! ', markup]
    return f"""
    **{post["title"]}**

Batafsil: {post["url"]}

😊 Bizga obuna bo'ling!!!
👉 [Texnorama](https://t.me/texnorama)
👉 [Instagram](https://www.instagram.com/texnorama.uz/)
👉 [Facebook](https://www.facebook.com/Texnoramauz-105786940766295/)
👉 [Twitter](https://twitter.com/texnorama)
    """

@logger.catch
@pub_service
def notify_by_telegram_channel(post):
    chat_id = Config.TELEGRAM_CHANNEL_CHAT_ID# CHANNEL ID
    print(f'========CHAT_ID = {chat_id}===============')
    # txt = order_details_text(order)
    txt = construct_message_text(post)
    # msg = bot.send_message(chat_id=chat_id, text=txt, parse_mode='Markdown')
    print(f"=====Feature image {post['feature_image']}=======")
    try:
        if post['feature_image']:
            msg = bot.send_photo(chat_id=chat_id, photo=post['feature_image'], caption=txt, parse_mode='Markdown')
            logger.success("============ Message <id: {}> is Sent with Captioned Photo ==================".format(msg.message_id))
        else:
            msg = bot.send_message(chat_id=chat_id, text=txt, parse_mode='Markdown')
            logger.success("\n============ Message  <id: {}> is Sent ==================".format(msg.message_id))
        return msg.message_id
    except Exception:
        logger.error("\n============! {} !==================".format(traceback.format_exc()))    
        return None


def edit_message_text(post, msg_id):
    chat_id = CHAT_ID# CHANNEL ID
    txt, markup = construct_message_text(post)
    try:
        bot.edit_message_text(message_id=msg_id,  chat_id=chat_id, text=txt, parse_mode='HTML', reply_markup=markup)
    except Exception as e:
        print(e)
    return "cool"

