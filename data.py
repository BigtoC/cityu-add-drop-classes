# coding=utf-8

import main

import time
from _datetime import datetime
from dataclasses import dataclass
import json

info_file = "info.json"
info = None
url = "https://banweb.cityu.edu.hk/pls/PROD/bwskfreg.P_AltPin"
login_url = "https://banweb.cityu.edu.hk/pls/PROD/twgkpswd_cityu.P_WWWLogin"
username: str
password: str
driver = None


@dataclass
class Info:
    time: time
    courses: list


def fetch_info():
    with open(info_file) as f:
        data = json.load(f)
        _time = datetime.strptime(data["time"], '%H:%M:%S')
        _course_list = data["courses"]

    global info
    info = Info(_time, _course_list)


def current_time() -> str:
    now_time = time.time()
    readable_time = datetime.fromtimestamp(now_time).strftime('[%H:%M:%S:%m] - ')
    return readable_time


if __name__ == '__main__':
    fetch_info()
    print(info.username)
