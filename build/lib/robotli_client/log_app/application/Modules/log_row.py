# -*-coding: utf8 -*-

from ..env import register_app
from ..env import requests, get_config

@register_app("dlog")
def dlog(info = ""):
    url = get_config("log_web_url")
    payload = "user_name=%s&user_passwd=%s&log=%s"%(get_config("user_name"), get_config("user_passwd"), info)
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    return response

