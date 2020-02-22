

class PubError(Exception):
    pass


pub_service_registrar = []


def pub_service(func):
    pub_service_registrar.append(func)
    return func


from .fb import send_fb_msg
from .texnobot import notify_by_telegram_channel
