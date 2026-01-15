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

    element = driver.find_element(By.XPATH, "//div/h6[contains(text(),'Payment Page')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    time.sleep(2)

    card_holder= driver.find_element(By.XPATH, "//input[@placeholder='John Doe']")
    card_holder.send_keys("Tejal")
    time.sleep(1)

    card_number = driver.find_element(By.ID, 'cardNumber')
    card_number.send_keys("1234123412341234")
    time.sleep(1)

    expiry_year = driver.find_element(By.ID, 'expiry')
    expiry_year.send_keys("0529")
    time.sleep(1)

    cvv = driver.find_element(By.ID, 'cvv')
    cvv.send_keys("123")
    time.sleep(1)

    submit = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit.click()
    time.sleep(5)








