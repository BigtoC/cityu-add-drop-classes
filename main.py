# coding=utf-8

import data
import add_drop_classes

from selenium import webdriver
import platform


def set_driver():
    # Set driver
    print(f"{data.current_time()}Setting up browser driver...")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('blink-settings=imagesEnabled==false')
    chrome_options.add_argument(f"user-agent={data.headers['User-Agent']}")

    driver = None
    if 'Windows' in platform.system():
        driver = webdriver.Chrome(executable_path='venv\chromedriver.exe', options=chrome_options)

    data.driver = driver
    print(f"{data.current_time()}Driver is set! \n")


def main():
    data.fetch_info()
    set_driver()
    print(f"{data.current_time()}This program will not store any personal info.")
    data.username = input(f"{data.current_time()}Input your EID: ")
    data.password = input(f"{data.current_time()}Input your password: ")
    print("")

    add_drop_classes.selenium_submit()


if __name__ == '__main__':
    main()
