#Day 48 of Udemy's 100 Days of Python programming course
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("")

email = driver.find_element(By.NAME, "email")
email.send_keys("")

button = driver.find_element(By.CSS_SELECTOR, "form button")

button.click()