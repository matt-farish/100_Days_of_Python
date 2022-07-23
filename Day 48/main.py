#Day 48 of Udemy's 100 Days of Python programming course
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver_path = "C:\Development\chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.python.org/")

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}

for n in range(0, len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)

driver.close()