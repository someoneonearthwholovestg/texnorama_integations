import json
from functools import wraps

from flask import request, Response
from datetime import datetime
from datetime import timedelta


class PostTask:
    def __init__(self, post_id, timeout=30):
        self.id = post_id
        self.timeout = timeout
        self.created_at = datetime.now()


POSTS_QUEUE = {}


class PostsQueue:
    def __init__(self):
        self._post_tasks = {}

    def __len__(self):
        return len(self._post_tasks)

    def __getitem__(self, i):
        self.clean_posts_queue()
        return self._post_tasks.get(i)

    def __setitem__(self, key, value):
        self._post_tasks[key] = value

    def clean_posts_queue(self):
        for key, item in self._post_tasks.copy().items():
            if item.created_at + timedelta(seconds=item.timeout) >= datetime.now():
                self._post_tasks.pop(key)


PQ = PostsQueue()


def idempotent(view):
    @wraps(view)
    def view_wrapper(*args, **kwargs):
        post = json.loads(request.data)['post']['current']
        if PQ[post["id"]]:
            return Response("Not Cool", 200)
        else:
            PQ[post["id"]] = PostTask(post["id"])
            return view(post)
    return view_wrapper
