# coding=utf-8

import time
from _datetime import datetime
import random


def current_time() -> str:
    now_time = time.time()
    readable_time = datetime.fromtimestamp(now_time).strftime('[%H:%M:%S:%m] - ')
    return readable_time


def random_wait():
    wait_time = random.uniform(0.5, 1.5)
    time.sleep(wait_time)

