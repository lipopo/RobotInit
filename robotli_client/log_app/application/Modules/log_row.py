# -*-coding: utf8 -*-

from ..env import register_app
from ..env import __log_url__, __user_name__, __user_passwd__, __mac_name__
from ..env import requests

@register_app("dlog")
def dlog(info = ""):
    url = __log_url__
    # info = "name:%s ip:%s time:%s"%( __mac_name__, ip, time.strftime("%Y-%m-%dT%H-%M-%S"))
    payload = "user_name=%s&user_passwd=%s&log=%s"%(__user_name__, __user_passwd__, info)
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    #print response.text
    return response

