from selenium import webdriver
import time
from selenium.webdriver.common.by import By


def test_idrive360_upgrade_prompt():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.idrive360.com/enterprise/login")
    time.sleep(2)

    user_email = driver.find_element(By.ID, "username")
    user_email.send_keys("augtest_040823@idrive.com")
    time.sleep(2)

    user_password = driver.find_element(By.ID, "password")
    user_password.send_keys("123456")
    time.sleep(2)


    signin_btn = driver.find_element(By.ID,"frm-btn")
    signin_btn.click()
    time.sleep(20)

    upgrade_msg = driver.find_element(By.ID, "upgrade")
    print(upgrade_msg.text)
    time.sleep(2)

    assert "Your free trial has expired\nUpgrade Now!" == upgrade_msg.text
    #assert "Upgrade Now!" == upgrade_msg.text
    time.sleep(2)

    driver.quit()
