#!/usr/bin/python
#-*- coding: utf8 -*-
from log_app import app as log_app
import thread
import time

if __name__ == "__main__":
    thread.start_new_thread(log_app.__call__, ())

    try:
        while True:
            time.sleep(3600 * 24)
    except:
        pass

