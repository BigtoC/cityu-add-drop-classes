# coding=utf-8

import data

import time
from bs4 import BeautifulSoup
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from decimal import Decimal, ROUND_HALF_UP


def selenium_submit():
    print(f"{data.current_time()}Getting web page source from {data.url} ...")
    data.driver.get(url=data.url)
    page = BeautifulSoup(data.driver.page_source, 'lxml').prettify()
    print(f"{data.current_time()}Got source! \n")

    if "to login AIMS." in page:
        login()

    # WebDriverWait(data.driver, 10).until(EC.title_contains("Add"))
    time.sleep(3)
    for item in data.cookies:
        data.driver.add_cookie(item)

    add_drop_page = BeautifulSoup(data.driver.page_source, 'lxml').prettify()
    print(add_drop_page)

    add_classes()


def login():
    print(f"{data.current_time()}Getting login web page source from {data.login_url} ...")
    data.driver.get(data.login_url)
    login_page = BeautifulSoup(data.driver.page_source, 'lxml').prettify()
    eid_name = get_eid_field_name(login_page)
    pwd_name = "p_password"
    button_name = "input_button"
    print(f"{data.current_time()}Got login page source! \n")

    print(f"{data.current_time()}Filling login information...")
    # Fill EID
    eid_field = data.driver.find_element_by_name(eid_name)
    eid_field.clear()
    eid_field.send_keys(data.username)

    # Fill password
    pwd_field = data.driver.find_element_by_name(pwd_name)
    pwd_field.clear()
    pwd_field.send_keys(data.password)

    # Click login button
    data.driver.find_element_by_class_name(button_name).click()
    print(f"{data.current_time()}Login success! \n")

    # Store Cookie
    data.cookies = data.driver.get_cookies()

# crn_id1, crn_id2
# find_element_by_id

def get_eid_field_name(page) -> str:
    name = re.search(r'User\d{14}', page)[0]
    return name


def add_classes():
    print("add classes")


if __name__ == "__main__":
    pass
