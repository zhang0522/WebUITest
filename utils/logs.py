# -*- encoding:utf-8 -*-
from config import DEBUG


def info(msg):
    print("[INFO] " + str(msg))


def debug(msg):
    if DEBUG == True:
        print("[DEBUG] " + str(msg))


def error(msg):
    print("[ERROR] " + str(msg))