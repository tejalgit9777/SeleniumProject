from selenium import webdriver
import pytest
import allure

@allure.title("Verify that we are able to open a page by using Selenium.")
@allure.description("We will open a page and verify that it is getting opened by using Selenium.")
def test_page_source():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    print(driver.title)
    print(driver.current_url)
    page_src = driver.page_source
    assert "CURA Healthcare Service" in page_src
    driver.quit()
