
from flask import Flask, jsonify
from flask import request
from texnobot import notify_by_telegram_channel
import json
from flask import Response

app = Flask(__name__)


@app.route('/newpost', methods=['GET', 'POST'])
def index():
    post = json.loads(request.data)['post']['current']
    notify_by_telegram_channel(post)
    return Response("Cool", 200)


if __name__ == '__main__':
    app.run(debug=True)
