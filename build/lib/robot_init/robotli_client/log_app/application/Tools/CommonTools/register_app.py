# -*- coding: utf8 -*-
from ...env import app

def register_app(call_name):

    def main(func):
        app.register_module(call_name, func)
        return func

    return main