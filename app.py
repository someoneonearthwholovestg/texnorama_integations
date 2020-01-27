
from flask import Flask
from setting import DB_CONNECTION_URL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_CONNECTION_URL

from views import new_post, update_post


app.add_url_rule('/newpost', 'publish', methods=['POST'], view_func=new_post)
app.add_url_rule('/updatepost', 'update', methods=['POST'], view_func=update_post)
