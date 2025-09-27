from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in/")

try:
    # Wait for search box to be present and find it
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='twotabsearchtextbox']"))
    )
    search_box.send_keys("iPhones")
    time.sleep(2)  # Brief pause to see results

    search_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='nav-search-submit-button']"))
    )
    time.sleep(2)
    search_button.click()
    time.sleep(2)

    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal']/span"))
    )
    print(element.text)
    # print("Span text:", span_element.text)
    #
    # # If you need to find multiple elements with the same xpath
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal']//span"))
    )
    for elem in elements:
        print(elem.text)
    time.sleep(2)

finally:
    driver.quit()