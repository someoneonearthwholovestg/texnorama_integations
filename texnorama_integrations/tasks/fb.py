from . import pub_service, PubError

from .. import graph
from .. import Config


@pub_service
def send_fb_msg(post):
	print('______________________________________________________________')
	print(post["title"], post["url"])
	try:
		graph.put_object(
		  parent_object=Config.FB_PAGE_ID,
		  connection_name="feed",
		  message=post["title"],
		  link=post["url"],
		)
	except Exception as e:
		raise PubError
