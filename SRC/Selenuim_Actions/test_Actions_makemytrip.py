import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton


@allure.title("Search in makeMyTrip")
@allure.description("Search in makeMyTrip")
def test_verify_action_makemytrip():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.makemytrip.com/")

    # //span[@data-cy="closeModal"] wait -> click
    WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH, "//span[@data-cy='closeModal']"))
    )
    driver.find_element(By.XPATH, "//span[@data-cy='closeModal']").click()
    time.sleep(2)

    WebDriverWait(driver=driver, timeout=3).until(
        EC.visibility_of_element_located((By.XPATH, "//img[@alt='minimize']"))

    )
    driver.find_element(By.XPATH, "//img[@alt='minimize']").click()
    #from City
    fromCity = driver.find_element(By.ID, "fromCity")

    background_element = driver.find_element(By.TAG_NAME, "body")
    background_element.click()

    actions_from = ActionChains(driver)
    (actions_from.
     move_to_element(fromCity)
     .click().send_keys_to_element(fromCity,"del")
     .perform())

    time.sleep(2)

    (actions_from.move_to_element(fromCity)
     .key_down(Keys.ARROW_DOWN)
     .key_down(Keys.ENTER).perform())

    # to City
    toCity = driver.find_element(By.ID, "toCity")

    actions_from = ActionChains(driver)
    (actions_from.
     move_to_element(toCity)
     .click().send_keys_to_element(toCity,"IXC")
     .perform())

    time.sleep(2)

    (actions_from.move_to_element(toCity)
     .key_down(Keys.ARROW_DOWN)
     .key_down(Keys.ENTER).perform())

    time.sleep(10)
