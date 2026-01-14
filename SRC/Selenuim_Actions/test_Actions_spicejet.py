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

@allure.title("Search in SpiceJet")
@allure.description("Search in SpiceJet from Delhi to Chandigarh")
def test_verify_action_SpiceJet():

    # chrome_options = Options()
    # chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.spicejet.com/")

    time.sleep(10)

    # WebDriverWait(driver=driver, timeout=5).until(
    #     EC.visibility_of_element_located((By.XPATH, '//div[contains(text(),"Welcome aboard")]'))
    # )

    from_city = driver.find_element(By.XPATH, '//div[@data-testid="to-testID-origin"]//input[@type="text"]')
    from_city.send_keys("del")
    time.sleep(2)

    to_city = driver.find_element(By.XPATH, '//div[@data-testid="to-testID-destination"]//input[@type="text"]')
    to_city.send_keys("ixc")
    time.sleep(2)

