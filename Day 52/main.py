#Day 52 of Udemy's 100 Days of Python programming course
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from decouple import config

DRIVER_PATH = Service("C:\Development\chromedriver.exe")
TARGET_ACCOUNT = config("TARGET_ACCOUNT")
USERNAME = config("ACCOUNT_USERNAME")
PASSWORD = config("PASSWORD")

class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service = driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.maximize_window()
        sleep(2)
        username_entry = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_entry.send_keys(USERNAME)
        password_entry = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_entry.send_keys(PASSWORD)
        password_entry.send_keys(Keys.ENTER)

    def find_followers(self):
        sleep(5)
        self.driver.get("https://www.instagram.com/goodguyfitz/followers/")
        sleep(5)

    def follow(self):
        people = self.driver.find_elements(By.CSS_SELECTOR, "li button")
        sleep(5)
        for person in people:
            if person.text == "Follow":
                person.click()
                sleep(3)
            
        self.driver.execute_script("argument[0].scrollIntoView(true);", people[-1])
        


follow_bot = InstaFollower(DRIVER_PATH)

follow_bot.login()
follow_bot.find_followers()
follow_bot.follow()

