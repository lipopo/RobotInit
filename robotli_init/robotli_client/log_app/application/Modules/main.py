# -*- coding: utf8 -*-
from ..env import os, time
from ..env import register_app, dlog, commands, get_config, row_render

@register_app("main")
def main():

    dlog("########## %s %s_IniT | \n\n"%(time.ctime(), get_config("mac_name")))

    for command in commands:
        dlog(command.command_name + "\n")
        
        start_exec = os.system(row_render.render(command.command))
        if start_exec == 0:
            dlog(command.command_success_msg+ "\n\n")
        else:
            dlog(command.command_fail_msg + "\n\n")
    dlog("Init finish~\n##########\n")
    return