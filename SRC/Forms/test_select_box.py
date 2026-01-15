#https://awesomeqa.com/practice.html
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

def test_select_box():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/practice.html")
    time.sleep(2)

    #First Name
    first_name = driver.find_element(By.XPATH, '//input[@name="firstname"]')
    time.sleep(2)
    actions = ActionChains(driver=driver)
    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name, "tejal").key_up(Keys.SHIFT).perform()

    #Last Name
    last_name = driver.find_element(By.XPATH, '//input[@name="lastname"]')
    last_name.send_keys("PATEL")
    time.sleep(2)
    # actions1 = ActionChains(driver=driver)
    # actions1.key_down(Keys.SHIFT).send_keys_to_element(last_name, "patel").key_up(Keys.SHIFT).perform()
    #select check box
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
    time.sleep(10)


