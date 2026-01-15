#https://the-internet.herokuapp.com/windows
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By

def test_multiple_browser_tabs():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/windows")
    time.sleep(2)

    link = driver.find_element(By.XPATH, "//a[contains(text(),'Click Here')]")
    link.click()
    time.sleep(2)

    driver.switch_to.window(driver.window_handles[1])
    print(driver.window_handles[1])
    print(driver.page_source)

    time.sleep(2)
    assert "New Window" in driver.page_source
    print("Test Completed")

    # txt_msg = driver.find_element(By.XPATH, '//div/h3[contains(text(),"New Window")]')
    # print(txt_msg.text)
    # assert "New Window" in txt_msg
    time.sleep(2)
    print("\n")
    driver.switch_to.window(driver.window_handles[0])
    print(driver.window_handles[0])
    #print(driver.page_source)
    assert "Click Here" in link.text
    print("Back to main window")

