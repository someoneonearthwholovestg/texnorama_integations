from .tasks import *
from flask import current_app as app

from flask import Response
from .models import db, Post
from .utils.idempotent import idempotent


@app.route('/newpost', methods=['POST'])
@idempotent
def new_post(post):
    if Post.query.filter_by(id=post["id"]).first():
        return Response("Not Cool", 200)

    for publish in pub_service_registrar:
        try:
            publish(post)
        except PubError as pe:
            # FIXME
            app.logger.info(f"Pub error in {publish.__name__}")

    post = Post(id=str(post["id"]))
    db.session.add(post)
    db.session.commit()

    return Response("Cool", 200)
