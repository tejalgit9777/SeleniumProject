# **Project 1 - Automating by using the Selenium Python. **
# 1. Navigate to the URL - [katalon-demo-cura.herokuapp.com](https://katalon-demo-cura.herokuapp.com/profile.php#login)
# 2. Find the **Make appointment** Button
# 3. Click on the **Make appointment **Button
# 4. Next Page will be loaded
# 5. **Find and Enter **the details **Username and Password** and **Click** on the Login Button
# 6. Verify current URL - [katalon-demo-cura.herokuapp.com/#appointment](https://katalon-demo-cura.herokuapp.com/#appointment)

import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def test_selenium_project_negative(make_appointment=None):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/profile.php")
    print(driver.title)

    make_appointment = driver.find_element(By.ID,"btn-make-appointment")
    make_appointment.click()
    time.sleep(2)

    user_name = driver.find_element(By.NAME,"username")
    user_name.send_keys("Tejal Patel")
    time.sleep(2)

    user_password = driver.find_element(By.NAME,"password")
    user_password.send_keys("TestPassword")
    time.sleep(2)

    login_btn = driver.find_element(By.ID,"btn-login")
    login_btn.click()
    time.sleep(2)

    error_msg = driver.find_element(By.CLASS_NAME,"text-danger")
    print(error_msg.text)
    time.sleep(2)
    assert "Login failed! Please ensure the username and password are valid." == error_msg.text
    time.sleep(2)

    driver.quit()


