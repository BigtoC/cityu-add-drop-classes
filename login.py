# coding=utf-8

import data
import common

import re
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def login():
    print(f"{common.current_time()}Getting login web page source from {data.login_url} ...")
    data.driver.get(data.login_url)
    login_page = BeautifulSoup(data.driver.page_source, 'lxml').prettify()
    eid_name = get_eid_field_name(login_page)
    pwd_name = "p_password"
    button_name = "input_button"
    print(f"{common.current_time()}Got login page source! \n")
    common.random_wait()

    print(f"{common.current_time()}Filling login information...")
    # Fill EID
    eid_field = data.driver.find_element_by_name(eid_name)
    eid_field.clear()
    eid_field.send_keys(data.username)
    print(f"{common.current_time()}Filled EID")
    common.random_wait()

    # Fill password
    pwd_field = data.driver.find_element_by_name(pwd_name)
    pwd_field.clear()
    pwd_field.send_keys(data.password)
    print(f"{common.current_time()}Filled password")
    common.random_wait()

    # Click login button
    data.driver.find_element_by_class_name(button_name).click()
    print(f"{common.current_time()}Clicked login")
    WebDriverWait(data.driver, 10).until_not(ec.title_contains("Login"))
    print(f"{common.current_time()}Login success! \n")


def get_eid_field_name(page) -> str:
    name = re.search(r'User\d{14}', page)[0]
    return name

