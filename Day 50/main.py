#Day 50 of Udemy's 100 Days of Python programming course
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from decouple import config

driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service = driver_path)

driver.get("https://tinder.com/")

sleep(3)

login_button = driver.find_element(By.CSS_SELECTOR, ".H\(40px\) .button")
login_button.click()

sleep(2)

login_w_facebook = driver.find_element(By.XPATH, '//*[@id="t-831228276"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
login_w_facebook.click()

sleep(3)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

PHONE = config("PHONE")
PASSWORD = config("PASSWORD")

email_entry = driver.find_element(By.XPATH, '//*[@id="email"]')
email_entry.send_keys(PHONE)

password_entry = driver.find_element(By.XPATH, '//*[@id="pass"]')
password_entry.send_keys(PASSWORD)
password_entry.send_keys(Keys.ENTER)

sleep(4)

driver.switch_to.window(base_window)
print(driver.title)