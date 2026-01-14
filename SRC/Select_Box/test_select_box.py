#https://awesomeqa.com/practice.html
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_select_box():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/practice.html")
    time.sleep(2)

    select_box_profession = driver.find_elements(By.XPATH, '//input[@name="profession"]')
    time.sleep(1)
    #select_box_profession[0].click()
    select_box_profession[1].click()
    time.sleep(1)

    select_box_automation_tool = driver.find_elements(By.XPATH, '//input[@name="tool"]')
    time.sleep(1)
    select_box_automation_tool[0].click()
    select_box_automation_tool[1].click()
    #select_box_automation_tool[2].click()
    time.sleep(2)


