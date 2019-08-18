# coding=utf-8

import data

import time
from datetime import datetime
from bs4 import BeautifulSoup
from decimal import Decimal, ROUND_HALF_UP


def selenium_submit(driver):
    print(f"{data.current_time()}Getting web page source from {data.url} ...")
    driver.get(data.url)
    page = BeautifulSoup(driver.page_source, 'lxml').prettify()
    print(f"{data.current_time()}Got source! \n")
    print(page)



def login():
    pass


if __name__ == "__main__":
    selenium_submit(data.driver)
