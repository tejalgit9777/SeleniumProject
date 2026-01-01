import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_VWO_login_error():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")

    user_email = driver.find_element(By.ID, "login-username")
    user_email.send_keys("admin@admin.com")
    time.sleep(2)
    user_password = driver.find_element(By.ID, "login-password")
    user_password.send_keys("admin")
    time.sleep(2)


    signin_btn = driver.find_element(By.ID,"js-login-btn")
    signin_btn.click()
    time.sleep(2)

    error_msg = driver.find_element(By.ID, "js-notification-box-msg")
    print(error_msg.text)
    time.sleep(2)

    assert "Your email, password, IP address or location did not match" == error_msg.text
    time.sleep(2)

    driver.quit()

