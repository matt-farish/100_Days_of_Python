#Day 49 of Udemy's 100 Days of Python programming course
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from decouple import config

linkedin_url = config("URL")
EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")

driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service = driver_path)

driver.get(linkedin_url)

time.sleep(4)

login_button = driver.find_element(By.CSS_SELECTOR, ".cta-modal__primary-btn")
login_button.click()

time.sleep(2)
user_name = driver.find_element(By.ID, "username")
user_name.send_keys(EMAIL)

password = driver.find_element(By.ID, "password")
password .send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

jobs = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")
for i in range(len(jobs)):
    try:
        each_job = driver.find_element(By.CLASS_NAME, f"jobs-search-two-pane__job-card-container--viewport-tracking-{i}")
    except NoSuchElementException:
        print("No company found")
        continue
    else:
        each_job.click()
        time.sleep(2)
        save_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply + .jobs-save-button")
        save_button.click()

time.sleep(3)
driver.quit()