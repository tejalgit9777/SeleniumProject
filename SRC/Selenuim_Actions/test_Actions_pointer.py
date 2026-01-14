import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@allure.title("Actions Draggable")
@allure.description("Verify pointer")
def test_verify_action_keyboard():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    # draggable
    element_to_hold = driver.find_element(By.ID, "draggable")

    # click - Normal Driver, will find the element and click on it. release it.
    # click and Hold - Actions Chains - Click and Hold (don'T RELEASE)
    time.sleep(2)

    actions = ActionChains(driver=driver)
    actions.click_and_hold(on_element=element_to_hold).perform()

    time.sleep(10)
