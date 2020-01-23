from urllib.parse import urljoin

import requests


class GhostContentClient:
    def __init__(self, url, api_key):
        self.url = url
        self.api_key = api_key

    @property
    def base_url(self):
        return f'https://{self.url}/ghost/api/v3/content/'

    def get_post(self, post_id=''):
        return requests.get(
            urljoin(self.base_url, f'posts/{post_id}'),
            params={'key': f'{self.api_key}'}
        )

    def get_latest_published_post(self):
        return requests.get(
            urljoin(self.base_url, f'posts/'),
            params={'key': f'{self.api_key}',
                    'fields': 'id,excerpt,title',
                    }
        )


gc = GhostContentClient('texnorama.uz', 'dea042c373b56c588b5802df70')

import json
rsp = gc.get_latest_published_post()

content_json = json.loads(rsp.content)
content_json
