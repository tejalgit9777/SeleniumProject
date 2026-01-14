from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains,ActionBuilder
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
import allure


@allure.title("Actions P2")
@allure.description("Verify MouseBack")
def test_verify_action_keyboard():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    atag_back = driver.find_element(By.ID, "click")
    atag_back.click()

    actions = ActionBuilder(driver=driver)
    actions.pointer_action.pointer_up(MouseButton.BACK)
    actions.perform()

    time.sleep(10)

