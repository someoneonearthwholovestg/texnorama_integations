import facebook
from settings import FB_GRAPH_API_TOKEN
from settings import FB_PAGE_ID


graph = facebook.GraphAPI(access_token=FB_GRAPH_API_TOKEN)


def send_fb_msg(post):
	print('______________________________________________________________')
	print(post["title"], post["url"])
	try:
		graph.put_object(
		  parent_object=FB_PAGE_ID,
		  connection_name="feed",
		  message=post["title"],
		  link=post["url"],
		)
	except Exception as e:
		print(e)
