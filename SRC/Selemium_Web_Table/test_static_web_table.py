# https://selectorshub.com/xpath-practice-page/
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import window
from selenium.webdriver.common.by import By

def test_static_web_table():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://selectorshub.com/xpath-practice-page/")
    time.sleep(1)

    userTable = driver.find_element(By.XPATH, "//h6[normalize-space()='User Table']")
    driver.execute_script("arguments[0].scrollIntoView(true);", userTable)
    time.sleep(2)

    rows= driver.find_elements(By.XPATH, "//table[@id='resultTable']/tbody/tr")
    total_rows = len(rows)
    print("Rows: ",total_rows)
    time.sleep(1)


    columns= driver.find_elements(By.XPATH, "//table[@id='resultTable']/tbody/tr[1]/td")
    total_columns = len(columns)
    print("Columns: ",total_columns)
    time.sleep(1)

    # for row in rows:
    #     print
    part1 = "//table[@id='resultTable']/tbody/tr["
    part2 = "]/td["
    part3 = "]"
    for i in range(1,total_rows + 1):
        for j in range(1,total_columns + 1):
            data = f"{part1}{i}{part2}{j}{part3}"
            #print(data)
            print(driver.find_element(By.XPATH, data).text)

