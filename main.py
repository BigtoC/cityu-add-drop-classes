# coding=utf-8

import data
import add_drop_classes

from selenium import webdriver
import platform


def set_driver():
    # Set driver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    print(f"{data.current_time()}Setting up browser driver...")

    driver = None
    if 'Windows' in platform.system():
        driver = webdriver.Chrome(executable_path='venv\chromedriver.exe', options=chrome_options)
    data.driver = driver

    print(f"{data.current_time()}Driver is set! \n")
    return driver


def main():
    data.fetch_info()
    set_driver()
    print(f"{data.current_time()}This program will not store any personal info.")
    data.username = input(f"{data.current_time()}Input your EID: ")
    data.password = input(f"{data.current_time()}Input your password: ")

    add_drop_classes.selenium_submit()


if __name__ == '__main__':
    main()
