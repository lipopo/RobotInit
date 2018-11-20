# -*- coding: utf8 -*-
from ..env import os, time
from ..env import BUCKET_PATH, __bucket_port__, __bucket_license__
from ..env import register_app, dlog

@register_app("main")
def main():
    dlog("########## %s PI001_IniT |"%(time.ctime()))

    start_frpc = os.system("nohup /home/pi/projects/frp/frp_0.21.0_linux_arm/frpc -c  /home/pi/projects/frp/jd_frp/jd_frp.ini & >> /tmp/logeryy")

    if start_frpc == 0:
        dlog(" Frpc 启动成功 |")
    else:
        dlog(" Frpc 启动失败 |")

    start_fakes3 = os.system("mkdir %s;nohup fakes3 -r %s -p %d --license %s &"%(BUCKET_PATH, BUCKET_PATH, __bucket_port__, __bucket_license__))
    if start_fakes3 == 0:
        dlog(" fakes3启动成功 端口为: %d |"%(__bucket_port__,))
    else:
        dlog(" FakeS3启动失败 |")
    start_redis = os.system("redish-server")
    dlog("Init finish~\n##########\n")
    return "a"
