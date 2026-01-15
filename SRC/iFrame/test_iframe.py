#https://selectorshub.com/iframe-scenario/
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By

def test_iframe():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selectorshub.com/iframe-scenario/")
    time.sleep(2)

    frame1 = driver.find_element(By.ID, "pact1")
    driver.switch_to.frame(frame1)
    time.sleep(2)

    first_crush = driver.find_element(By.XPATH,'//div/input[@placeholder="First Crush"]')
    first_crush.send_keys('Test Test')
    time.sleep(2)

    frame2 = driver.find_element(By.ID, "pact2")
    driver.switch_to.frame(frame2)
    time.sleep(2)

    current_crush_name = driver.find_element(By.ID,'jex')
    current_crush_name.send_keys('Test Test')
    time.sleep(2)

    frame3 = driver.find_element(By.ID, "pact3")
    driver.switch_to.frame(frame3)
    time.sleep(2)

    destiny = driver.find_element(By.ID,'glaf')
    destiny.send_keys('Test Destiny')
    time.sleep(2)

    #back to first frame
    # driver.switch_to.parent_frame()
    # driver.switch_to.parent_frame()
    driver.switch_to.default_content()
    driver.switch_to.frame(frame1)

    time.sleep(2)
    first_crush.clear()
    first_crush.send_keys('Test First')

    time.sleep(2)



