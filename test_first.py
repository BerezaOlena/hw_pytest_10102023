from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
def test_google_search():
    driver = webdriver.Chrome()
    try:
        driver.get("https://google.com")
        time.sleep(5)
        textarea = driver.find_element(By.NAME, "q")
        textarea.send_keys("IT_step")
        textarea.send_keys(Keys.ENTER)
        time.sleep(10)
    finally:
        driver.quit()

