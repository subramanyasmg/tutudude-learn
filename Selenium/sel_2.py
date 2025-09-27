from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize Chrome driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")

try:
    # Wait for search box to be present and find it
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
    )

    # Type "python" in search box
    search_box.send_keys("python")

    # Press Enter to search (more reliable than clicking button)
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    time.sleep(2)  # Brief pause to see results

    # Navigate back and forward
    driver.back()
    time.sleep(3)
    driver.forward()
    time.sleep(3)

finally:
    driver.quit()