
from flask import Flask, jsonify
from flask import request
from texnobot import notify_by_telegram_channel
import json
from flask import Response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    msg_id = db.Column(db.Integer)


@app.route('/newpost', methods=['POST'])
def index():
    post = json.loads(request.data)['post']['current']
    if Post.query.filter_by(id=post["id"]).first():
        return Response("Not Cool", 200)
    message_id = notify_by_telegram_channel(post)
    Post(id=str(post["id"]), msg_id=message_id)
    return Response("Cool", 200)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
