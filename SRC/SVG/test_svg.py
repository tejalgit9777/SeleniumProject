#https://www.amcharts.com/svg-maps/?map=india
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_svg():
    driver = webdriver.Chrome()
    #driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    #time.sleep(2)

    driver.find_element(By.XPATH, "//button[contains(text(),'I understand and agree')]").click()
    time.sleep(1)
    state_list = driver.find_elements(By.XPATH, "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")

    for state in state_list:
        state.get_attribute("aria-label")
        print(state.get_attribute("aria-label"))
        #time.sleep(2)
        if "Maharashtra  " in state.get_attribute("aria-label"):
            state.click()

            # To verify state name, tooltip
            tooltip_text = state.get_attribute("aria-label")
            assert "Maharashtra" in tooltip_text
            print("Tooltip verified:", tooltip_text)
            break

    time.sleep(5)



