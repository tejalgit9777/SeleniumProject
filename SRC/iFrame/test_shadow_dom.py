# https://selectorshub.com/xpath-practice-page/
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By


def test_shadow_dom():
    # driver = webdriver.Edge()
    # driver = webdriver.Firefox()
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selectorshub.com/xpath-practice-page/")
    time.sleep(2)

    shadow_dom_element = driver.find_element(By.XPATH, "//div/h6[contains(text(),'Shadow DOM')]")
    driver.execute_script("arguments[0].scrollIntoView(true);", shadow_dom_element)
    time.sleep(2)

    kills_input = driver.execute_script(
        "return    document.querySelector('div#userName').shadowRoot.querySelector('input#kils')")
    kills_input.send_keys("Test Username")
    time.sleep(2)

    pizza_input = driver.execute_script(
        "return    document.querySelector('div#userName').shadowRoot.querySelector('#app2').shadowRoot.querySelector('#pizza');")
    pizza_input.send_keys("Test Pizza")
    time.sleep(2)


    # # 1. Locate the shadow host element
    # shadowroot1 = driver.find_element(By.ID, "userName")
    #
    # # 2. Access the shadow root
    # shadow_root_1 = shadowroot1.shadow_root
    #
    # username = shadow_root_1.find_element(By.ID, "kils")
    # username.send_keys("Test name")
    #
    # time.sleep(2)
    #
    # shadowroot2 = shadow_root_1.find_element(By.ID, "app2")
    # shadow_root_2 = shadowroot2.shadow_root
    #
    # pizza_name= shadow_root_2.find_element(By.ID, "pizza")
    # pizza_name.send_keys("Margarita")
    # time.sleep(2)

    # shadowroot3 = shadow_root_1.find_element(By.ID, "concepts")
    # shadow_root_3 = shadowroot3.shadow_root
    #
    # concepts = shadow_root_3.find_element(By.ID, "training")
    # concepts.send_keys("Test Training")
    # time.sleep(2)
