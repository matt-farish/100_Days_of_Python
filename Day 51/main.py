#Day 51 of Udemy's 100 Days of Python programming course
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
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
        self.driver.get("https://www.speedtest.net/")
        sleep(2)
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()
        sleep(50)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div\
            /div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2\
                ]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/d\
            iv/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/\
                span').text

    def tweet(self):
        self.driver.get("https://twitter.com/")
        sleep(2)
        sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/\
            div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
        sign_in_button.click()

        sleep(5)

        email_entry = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/\
            div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/di\
                v[2]/div/input')
        email_entry.send_keys(TWITTER_EMAIL)
        email_entry.send_keys(Keys.ENTER)

        sleep(10)

        password_entry = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/d\
            iv/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/la\
                bel/div/div[2]/div[1]/input')
        password_entry.send_keys(TWITTER_PASSWORD)
        password_entry.send_keys(Keys.ENTER)

        sleep(5)

        tweet_field = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div\
            [2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div\
                [1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]\
                    /div/div/div/div')
        message = f"Why does my Internet speed suck so much? I should be getting {TARGET_DOWN} \
            down | {TARGET_UP} UP, and instead im getting {self.down} down | {self.up} up."
        tweet_field.send_keys(message)

        send_tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/d\
            iv/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[\
                2]/div[3]/div/div/div[2]/div[3]')
        send_tweet_button.click()
    
    def close(self):
        sleep(5)
        self.driver.quit()


bot = InternetSpeedTwitterBot(DRIVER_PATH)

bot.get_internet_speed()
bot.tweet()

bot.close()