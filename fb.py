import facebook
from setting import FB_GRAPH_API_TOKEN
from setting import FB_PAGE_ID


graph = facebook.GraphAPI(access_token=FB_GRAPH_API_TOKEN)

def send_fb_msg(post):
	print('______________________________________________________________')
	print(post["title"], post["url"])
	graph.put_object(
	  parent_object=FB_PAGE_ID,
	  connection_name="feed",
	  message=post["title"],
	  link="http://texnorama/marsdagi-zararsiz-tez-ovqatlanish-va-hayot-odamlar-2020-yilni-qanday-tasavvur-qilishdi/",
	)

