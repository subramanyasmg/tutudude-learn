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
        EC.presence_of_element_located((By.LINK_TEXT, "Electronics"))
    )

    search_box.click()

    time.sleep(2)  # Brief pause to see results

    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Audio"))
    )
    search_box.click()
    time.sleep(2)

    driver.refresh()

finally:
    driver.quit()