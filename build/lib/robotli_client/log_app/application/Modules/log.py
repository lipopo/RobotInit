# -*-coding: utf8 -*-

from ..env import register_app
from ..env import requests, time, get_config

@register_app("log")
def log(ip):
    url = get_config("status_web_url")
    info = "name:%s ip:%s time:%s"%( get_config("mac_name"), ip, time.strftime("%Y-%m-%dT%H-%M-%S"))
    payload = "user_name=%s&user_passwd=%s&status=%s"%(get_config("user_name"), get_config("user_passwd"), info)
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    #print response.text
    return response

