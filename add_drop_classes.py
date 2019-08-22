# coding=utf-8

import data
from login import login

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import selenium.common.exceptions


def selenium_submit():
    wait_until()
    add_classes()


def navigate_to():
    """
        Navigation path:
        Personal Information -> Course Registration -> Add or Drop Classes -> Registration Term -> Add or Drop Classes
    """
    print(f"{data.current_time()}Navigating to add/drop page... \n")
    # Click: Course Registration
    data.driver.find_elements_by_xpath("//*[contains(text(), 'Course Registration')]")[0].click()
    print(f"{data.current_time()}Click: Course Registration")
    WebDriverWait(data.driver, 10).until(ec.title_contains("Course Registration"))
    data.random_wait()

    # Click: Add or Drop Classes
    data.driver.find_elements_by_xpath("//*[contains(text(), 'Add or Drop Classes')]")[0].click()
    print(f"{data.current_time()}Click: Add or Drop Classes")
    WebDriverWait(data.driver, 10).until(ec.title_contains("Registration Term"))
    data.random_wait()

    # Click: submit
    data.driver.find_elements_by_xpath("//*[@value='Submit']")[0].click()
    print(f"{data.current_time()}Click: submit")
    WebDriverWait(data.driver, 10).until(ec.title_contains("Add or Drop Classes"))

    if "You may register during the following times:" in data.driver.page_source:
        print(f"{data.current_time()}Got add/drop page! "
              f"Please wait {data.info.start_timestamp - int(time.time())} seconds... \n")


def wait_until():
    now = int(time.time())
    waiting = data.info.start_timestamp - now

    if now < data.info.start_timestamp:
        print(f"{data.current_time()}Please wait {waiting} seconds "
              f"until {data.info.start_time}, "
              f"during the time, do not close this program. \n")

        if waiting >= 300:
            time.sleep(waiting - 299)
            print(f"{data.current_time()}5 minutes to {data.info.start_time}, now login! \n")
            login()
            navigate_to()
        else:
            print(f"{data.current_time()}Less than 5 minutes to {data.info.start_time}, now login! \n")
            login()
            navigate_to()
            time.sleep(waiting - 5)

        while int(time.time()) <= data.info.start_timestamp - 1:
            time.sleep(0.1)
    else:
        print(f"{data.current_time()}Now login! \n")
        login()
        navigate_to()


def add_classes():
    print(f"{data.current_time()}Refreshing! \n")
    data.driver.refresh()
    try:
        data.driver.switch_to.alert.accept()
    except selenium.common.exceptions.NoAlertPresentException:
        pass

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
