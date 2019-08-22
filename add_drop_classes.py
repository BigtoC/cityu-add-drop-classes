# coding=utf-8

import data

import time
from bs4 import BeautifulSoup
import re
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import random


def selenium_submit():
    login()
    WebDriverWait(data.driver, 10).until_not(ec.title_contains("Login"))

    '''
    Navigation path: 
       Personal Information -> Course Registration -> Add or Drop Classes -> Registration Term -> Add or Drop Classes
    '''
    print(f"{data.current_time()}Navigating to add/drop page... \n")
    # Click: Course Registration
    data.driver.find_elements_by_xpath("//*[contains(text(), 'Course Registration')]")[0].click()
    WebDriverWait(data.driver, 10).until(ec.title_contains("Course Registration"))
    random_wait()

    # Click: Add or Drop Classes
    data.driver.find_elements_by_xpath("//*[contains(text(), 'Add or Drop Classes')]")[0].click()
    WebDriverWait(data.driver, 10).until(ec.title_contains("Registration Term"))
    random_wait()

    # Click: submit
    data.driver.find_elements_by_xpath("//*[@value='Submit']")[0].click()
    WebDriverWait(data.driver, 10).until(ec.title_contains("Add or Drop Classes"))

    if "You may register during the following times:" in data.driver.page_source:
        print(f"{data.current_time()}Got add/drop page and wait! \n")

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
    random_wait()

    # Fill password
    pwd_field = data.driver.find_element_by_name(pwd_name)
    pwd_field.clear()
    pwd_field.send_keys(data.password)
    random_wait()

    # Click login button
    data.driver.find_element_by_class_name(button_name).click()
    print(f"{data.current_time()}Login success! \n")


def get_eid_field_name(page) -> str:
    name = re.search(r'User\d{14}', page)[0]
    return name


def wait_until():
    now = int(time.time())
    waiting = data.info.start_timestamp - now
    if now < data.info.start_timestamp:
        print(f"{data.current_time()}Please wait {waiting} seconds until {data.info.time}...")
        time.sleep(waiting - 5)

    while int(time.time()) < data.info.start_timestamp:
        time.sleep(0.1)


def random_wait():
    wait_time = random.uniform(0.2, 1.1)
    time.sleep(wait_time)


def add_classes():
    wait_until()
    data.driver.refresh()
    if "You may register during the following times" in data.driver.page_source:
        print(f"{data.current_time()}Please check time you set in info.json!")
        print(f"{data.current_time()}This program will quit now, please rerun this after you edit the time. \n")
        return

    # Now enter add/drop page
    print(f"{data.current_time()}Now enter add/drop page")
    total_courses_num = len(data.info.courses)

    print(f"{data.current_time()}Filling CRNs...")
    for i in range(total_courses_num):
        crn_field = data.driver.find_element_by_id(f"crn_id{i + 1}")
        crn_field.clear()
        crn_field.send_keys(data.info.courses[i])

    # Click: submit
    data.driver.find_elements_by_xpath("//*[@value='Submit Changes']")[0].click()
    WebDriverWait(data.driver, 10).until(ec.title_contains("Add or Drop Classes"))

    if "Registration Add Errors" in data.driver.page_source:
        print(f"{data.current_time()}Registration Add Errors, please login AIMS for details")
    else:
        print(f"{data.current_time()}Added classes!")


if __name__ == "__main__":
    pass
