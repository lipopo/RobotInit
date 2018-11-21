# -*- coding: utf8 -*-

from ..log_app import app as log_app
import thread
import time

def main():
    thread.start_new_thread(log_app.__call__, ())

    try:
        while True:
            time.sleep(3600 * 24)
    except:
        pass