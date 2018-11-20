# -*- coding: utf8 -*-

# os工具
import os

"""
静态资源
"""
__web_url__ = "http://www.lipocmma.cn:16616/log_web"
__log_url__ = __web_url__ + "/log"
__status_url__ = __web_url__ + "/status"

__user_name__ = "lipo"
__user_passwd__ = "lipo8081"

__mac_name__ = "树莓小PI001"
STATIC_PATH = os.path.join(os.path.dirname(__file__), "Static")

BUCKET_PATH = "/tmp/buckets"
__bucket_port__ = 8991
__bucket_license__ = "8069351278"

exec_command = "ifconfig eth0 | grep 'netmask' | awk '{print $2}'"
"""
动态共享资源
"""

"""
工具箱
"""

# 公用工具箱
import requests
import time

# 本地工具箱
"""
应用初始化部分------------------------------------------------
"""
# 生成app handler
from .Tools.CommonTools.app import APP
# 初始化应用
app = APP()

# 导入注册工具
from .Tools.CommonTools.register_app import register_app

# 导入log函数
from .Modules.log import log
# 导入dlog
from .Modules.log_row import dlog

# 导入main函数
from .Modules.main import main

# 导入主函数
from .app import call

"""
------------------------------------------------------------
"""
