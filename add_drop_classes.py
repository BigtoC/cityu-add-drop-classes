# coding=utf-8

import data

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def selenium_submit():
    WebDriverWait(data.driver, 10).until_not(ec.title_contains("Login"))

    '''
    Navigation path: 
       Personal Information -> Course Registration -> Add or Drop Classes -> Registration Term -> Add or Drop Classes
    '''
    print(f"{data.current_time()}Navigating to add/drop page... \n")
    # Click: Course Registration
    data.driver.find_elements_by_xpath("//*[contains(text(), 'Course Registration')]")[0].click()
    WebDriverWait(data.driver, 10).until(ec.title_contains("Course Registration"))
    data.random_wait()

    # Click: Add or Drop Classes
    data.driver.find_elements_by_xpath("//*[contains(text(), 'Add or Drop Classes')]")[0].click()
    WebDriverWait(data.driver, 10).until(ec.title_contains("Registration Term"))
    data.random_wait()

    # Click: submit
    data.driver.find_elements_by_xpath("//*[@value='Submit']")[0].click()
    WebDriverWait(data.driver, 10).until(ec.title_contains("Add or Drop Classes"))

    if "You may register during the following times:" in data.driver.page_source:
        print(f"{data.current_time()}Got add/drop page and wait! \n")

    add_classes()


def wait_until():
    now = int(time.time())
    waiting = data.info.start_timestamp - now
    if now < data.info.start_timestamp:
        print(f"{data.current_time()}Please wait {waiting} seconds until {data.info.time}...")
        time.sleep(waiting - 5)

    while int(time.time()) < data.info.start_timestamp:
        time.sleep(0.1)


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
        print(f"{data.current_time()}Added courses: {data.info.courses}")


if __name__ == "__main__":
    pass
