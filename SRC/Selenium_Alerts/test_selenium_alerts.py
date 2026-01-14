# https://the-internet.herokuapp.com/javascript_alerts
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_selenium_alert():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    time.sleep(2)

    js_alert = driver.find_element(By.XPATH, '//button[contains(text(),"Click for JS Alert")]')
    # driver.implicitly_wait(5)
    time.sleep(2)
    js_alert.click()
    time.sleep(2)
    alert = driver.switch_to.alert
    alert.accept()

    result = driver.find_element(By.ID, "result")
    assert result.text == "You successfully clicked an alert"
    time.sleep(1)

def test_selenium_Confirm_alert():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    time.sleep(2)

    js_alert = driver.find_element(By.XPATH, '//button[contains(text(),"Click for JS Confirm")]')
    # driver.implicitly_wait(5)
    # webdriverwait = WebDriverWait(driver=driver, timeout=10).until(EC.visibility_of_element_located())
    time.sleep(2)
    js_alert.click()
    time.sleep(2)
    alert = driver.switch_to.alert
    alert.accept()

    result = driver.find_element(By.ID, "result")
    assert result.text == "You clicked: Ok"
    time.sleep(1)

def test_selenium_prompt_alert():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    driver.maximize_window()
    time.sleep(2)

    js_alert = driver.find_element(By.XPATH, '//button[contains(text(),"Click for JS Prompt")]')
    # driver.implicitly_wait(5)
    # webdriverwait = WebDriverWait(driver=driver, timeout=10).until(EC.visibility_of_element_located())
    time.sleep(2)
    js_alert.click()
    time.sleep(2)
    alert = driver.switch_to.alert
    alert.send_keys("Test prompt text")
    time.sleep(2)
    alert.accept()

    result = driver.find_element(By.ID, "result")
    assert result.text == "You entered: Test prompt text"
    time.sleep(1)