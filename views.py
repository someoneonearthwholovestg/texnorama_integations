from flask import jsonify
from flask import request
from fb import send_fb_msg
from texnobot import notify_by_telegram_channel
from texnobot import edit_message_text
import json
from flask import Response
from models import db, Post


def new_post():
    post = json.loads(request.data)['post']['current']
    print(post['id'])
    if Post.query.filter_by(id=post["id"]).first():
        return Response("Not Cool", 200)
    message_id = notify_by_telegram_channel(post)
    send_fb_msg(post)

    post = Post(id=str(post["id"]), msg_id=message_id)
    db.session.add(post)
    db.session.commit()
    return Response("Cool", 200)


def update_post():
    post = json.loads(request.data)['post']['current']
    p = Post.query.filter_by(id=post["id"]).first()
    print(p)
    msg_id = p.msg_id
    try:
        edit_message_text(post, msg_id)
    except Exception as e:
        print(e)
    return Response("Cool", 200)
