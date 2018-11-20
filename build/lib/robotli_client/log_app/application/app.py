# -*- coding: utf8 -*-
from .env import register_app
from .env import log, main
from .env import exec_command
from .env import time, os

@register_app("__call__")
def call():
    # 初始化流程:
    main()
    while True:
        get_ip_info = os.popen(exec_command)
        read_data = get_ip_info.readline()
        if read_data != "":
            log(read_data[:-1])
        # else:
            #f.write("不能获取ip信息，请确定使用Lin")
        time.sleep(10)
