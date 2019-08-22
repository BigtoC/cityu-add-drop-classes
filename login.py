# coding=utf-8

import data

import re
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def login():
    print(f"{data.current_time()}Getting login web page source from {data.login_url} ...")
    data.driver.get(data.login_url)
    login_page = BeautifulSoup(data.driver.page_source, 'lxml').prettify()
    eid_name = get_eid_field_name(login_page)
    pwd_name = "p_password"
    button_name = "input_button"
    print(f"{data.current_time()}Got login page source! \n")
    data.random_wait()

    print(f"{data.current_time()}Filling login information...")
    # Fill EID
    eid_field = data.driver.find_element_by_name(eid_name)
    eid_field.clear()
    eid_field.send_keys(data.username)
    print(f"{data.current_time()}Filled EID")
    data.random_wait()

    # Fill password
    pwd_field = data.driver.find_element_by_name(pwd_name)
    pwd_field.clear()
    pwd_field.send_keys(data.password)
    print(f"{data.current_time()}Filled password")
    data.random_wait()

    # Click login button
    data.driver.find_element_by_class_name(button_name).click()
    print(f"{data.current_time()}Clicked login")
    WebDriverWait(data.driver, 10).until_not(ec.title_contains("Login"))
    print(f"{data.current_time()}Login success! \n")


def get_eid_field_name(page) -> str:
    name = re.search(r'User\d{14}', page)[0]
    return name

