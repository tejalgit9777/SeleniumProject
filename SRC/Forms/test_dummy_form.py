#https://selectorshub.com/xpath-practice-page/
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By

def test_select_box():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selectorshub.com/xpath-practice-page/")
    time.sleep(2)

    email= driver.find_element(By.XPATH, "//input[@name='email']")
    email.send_keys("test150126@yopmail.com")
    time.sleep(1)

    password = driver.find_element(By.XPATH, "//input[@name='Password']")
    password.send_keys("Test@123")
    time.sleep(1)

    company = driver.find_element(By.XPATH, "//input[@name='company']")
    company.send_keys("Test Infotech")
    time.sleep(1)

    mobile = driver.find_element(By.XPATH, "//input[@name='mobile number']")
    mobile.send_keys("4365755757")
    time.sleep(1)

    country = driver.find_element(By.XPATH, "//div/label/input[@type='text']")
    country.send_keys("India")
    time.sleep(1)

    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(1)

    submit = driver.find_element(By.XPATH, "//button[@value='Submit']")
    submit.click()
    time.sleep(5)








