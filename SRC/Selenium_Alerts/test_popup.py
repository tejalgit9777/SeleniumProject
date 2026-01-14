#https://www.makemytrip.com/
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_popup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.makemytrip.com/")

    WebDriverWait(driver=driver, timeout=10).until(EC.visibility_of_element_located((By.XPATH, '//span[@data-cy="closeModal"]')))

    popup = driver.find_element(By.XPATH, '//span[@data-cy="closeModal"]')
    popup.click()
    time.sleep(2)


