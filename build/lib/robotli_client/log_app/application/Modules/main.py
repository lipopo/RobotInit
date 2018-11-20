# -*- coding: utf8 -*-
from ..env import os, time
from ..env import register_app, dlog, commands, ConfigTemplate, all_configs, get_config

@register_app("main")
def main():
    dlog("########## %s %s_IniT | \n\n"%(time.ctime(), get_config("mac_name")))

    for command in commands:
        dlog(command.command_name + "\n")
        start_exec = os.system(ConfigTemplate(all_configs, command.command).render_value)
        if start_exec == 0:
            dlog(command.command_success_msg+ "\n\n")
        else:
            dlog(command.command_fail_msg + "\n\n")
    dlog("Init finish~\n##########\n")
    return "a"
