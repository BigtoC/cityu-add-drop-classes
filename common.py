# coding=utf-8

import data

import time
from _datetime import datetime
import random
import os


def current_time() -> str:
    now_time = time.time()
    readable_time = datetime.fromtimestamp(now_time).strftime('[%H:%M:%S:%m] - ')
    return readable_time


def random_wait():
    wait_time = random.uniform(0.5, 1.5)
    time.sleep(wait_time)


def logger(msg: str):
    dir_name = "logs"
    log_msg = f"{msg} \n"
    mkdir(dir_name)
    try:
        data.log_file_name
    except AttributeError:
        now_time = time.time()
        data.log_file_name = datetime.fromtimestamp(now_time).strftime('%Y-%m-%d_%H-%M-%S')
    with open(f"{dir_name}/{data.log_file_name}.txt", "a") as lf:
        lf.write(f"{current_time()}{log_msg}")
        lf.close()
    print(f"{current_time()}{msg}")


def mkdir(pathname: str) -> bool:
    # Delete the first space character
    path = pathname.strip()
    # Delete '\' symbol
    path = path.rstrip("\\")

    # Check if the path exists
    is_exists = check_existing(path)

    if not is_exists:
        os.makedirs(path)
        return True
    else:
        return False


def check_existing(name: str) -> bool:
    return os.path.exists(name)


if __name__ == '__main__':
    logger('hahaha')
    logger('lalala')
    logger('hhh')
