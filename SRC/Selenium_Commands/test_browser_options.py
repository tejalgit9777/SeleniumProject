from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
import allure
import time

def test_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    #chrome_options.add_argument("--headless")
    #chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=1000,700")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print(driver.title)
    time.sleep(5)
    driver.quit()
