# -*- coding: utf8 -*-

# os工具
import os

"""
静态资源
"""
STATIC_PATH = os.path.join(os.path.dirname(__file__), "Static")
STATIC_FILES_PATH = os.path.join(STATIC_PATH, "Files")

# 配置文件目录
CONFIG_FILE_PATH = os.path.join(STATIC_FILES_PATH, "config.yaml")

"""
动态共享资源
"""

"""
工具箱
"""

# 公用工具箱
import requests
import time
import jinja2
import yaml
from collections import namedtuple

# 本地工具箱
from .Tools.CommonTools.template import ConfigTemplate
from .Tools.CommonTools.translate_config import translate_config
"""
配置文件加载-------------------------------------------------
"""
Config = namedtuple("Config", ["commands"])
CommandConfig = namedtuple("CommandConfig", ["command_name", "command", "command_success_msg", "command_fail_msg"])

config_dict = yaml.load(open(CONFIG_FILE_PATH if os.path.exists(CONFIG_FILE_PATH) else os.path.join(".", "config.yaml"), "r"))
all_configs = translate_config(None, config_dict)
get_config = lambda config_name: ConfigTemplate(config_dict=all_configs, source=str(all_configs.get(config_name, ""))).render_value
config = Config(commands=config_dict.get("commands_exec", []))

# 指令列表
commands = [
    CommandConfig(**command)
    for command in config.commands
]

"""
------------------------------------------------------------
"""

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
