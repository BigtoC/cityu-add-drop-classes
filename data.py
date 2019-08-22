# coding=utf-8

import time
from _datetime import datetime
from dataclasses import dataclass
import json

info_file = "info.json"
info = None
login_url = "https://banweb.cityu.edu.hk/pls/PROD/twgkpswd_cityu.P_WWWLogin"
username: str
password: str
driver = None
headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-HK,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-HK;q=0.6,en-US;q=0.5,ja;q=0.4',
        'Connection': 'keep-alive',
        'Content-Type': 'text/plain; charset=UTF-8',
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'
    }


@dataclass
class Info:
    time: time
    start_timestamp: time
    courses: list


def fetch_info():
    # Load time and CRNs from json file
    with open(info_file) as f:
        data = json.load(f)
        _time = datetime.strptime(data["time"], '%Y-%m-%d %H:%M:%S')
        _course_list = data["courses"]

    _timestamp = int(time.mktime(_time.timetuple()))
    global info
    info = Info(_time, _timestamp, _course_list)


def current_time() -> str:
    now_time = time.time()
    readable_time = datetime.fromtimestamp(now_time).strftime('[%H:%M:%S:%m] - ')
    return readable_time


if __name__ == '__main__':
    fetch_info()
    print(info.username)
