import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def test_verify_actions_key():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    time.sleep(1)
    first_name = driver.find_element(By.XPATH, '//input[@name="firstname"]')
    #time.sleep(2)
    actions = ActionChains(driver=driver)

    actions.key_down(Keys.SHIFT).send_keys_to_element(first_name, "action chains test").key_up(Keys.SHIFT).perform()

    time.sleep(5)
