#Day 51 of Udemy's 100 Days of Python programming course
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from decouple import config

TARGET_DOWN = 70
TARGET_UP = 25
TWITTER_EMAIL = config("EMAIL")
TWITTER_PASSWORD = config("PASSWORD")
DRIVER_PATH = Service("C:\Development\chromedriver.exe")

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service = driver_path)
        self.up = 0
        self.down = 0


    def get_internet_speed(self):
        pass


    def tweet(self):
        pass

bot = InternetSpeedTwitterBot(DRIVER_PATH)

bot.get_internet_speed()
bot.tweet()