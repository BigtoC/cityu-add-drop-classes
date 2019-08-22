# coding=utf-8

import data
from add_drop_classes import selenium_submit
import common

from selenium import webdriver
import platform


def set_driver():
    # Set driver
    common.logger("Setting up browser driver...")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.headless = True
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('blink-settings=imagesEnabled==false')  # Not loading images
    chrome_options.add_argument('--log-level=3')  # Disable logs issued by Chrome
    chrome_options.add_argument(f"user-agent={data.headers['User-Agent']}")

    driver = None
    if 'Windows' in platform.system():
        driver = webdriver.Chrome(executable_path='venv\chromedriver.exe', options=chrome_options)

    data.driver = driver
    common.logger("Driver is set! \n")


def main():
    data.fetch_info()

    print(f"{common.current_time()}This program will not store any personal info.")
    data.username = input(f"{common.current_time()}Input your EID: ")
    data.password = input(f"{common.current_time()}Input your password: ")
    print("")

    set_driver()

    selenium_submit()

    data.driver.quit()

    input(f"{common.current_time()}Press any key to quit!")


if __name__ == '__main__':
    main()
