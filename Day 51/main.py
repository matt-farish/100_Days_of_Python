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

# Class that handles all the bot behaviour
class InternetSpeedTwitterBot:
    # Initialise the driver and starting values for the upload and download numbers
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service = driver_path)
        self.up = 0
        self.down = 0

    # Function for retrieving the download and upload speed values.
    def get_internet_speed(self):
        # Open the Ookla Speedtest site.
        self.driver.get("https://www.speedtest.net/")
        # Allow time for the page to open.
        sleep(2)
        # Find and click on the button to start the speed test.
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()
        # Allow time for the test to complete.
        sleep(50)
        # Retrieve the values for the download and upload speeds.
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div\
            /div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2\
                ]/span').text
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/d\
            iv/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/\
                span').text

    # Function for logging into Twitter before composing and sending a tweet.
    def tweet(self):
        # Open the Twitter page.
        self.driver.get("https://twitter.com/")
        # Allow time for the page to load.
        sleep(2)
        # Find and click the sign in button.
        sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/\
            div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
        sign_in_button.click()
        #Allow time for the page to load.
        sleep(5)
        # Find the email entry field, enter the email and press enter.
        email_entry = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/\
            div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/di\
                v[2]/div/input')
        email_entry.send_keys(TWITTER_EMAIL)
        email_entry.send_keys(Keys.ENTER)
        # Allow time for the page to load.
        sleep(10)
        # Find the password entry field, enter the password and press enter.
        password_entry = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/d\
            iv/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/la\
                bel/div/div[2]/div[1]/input')
        password_entry.send_keys(TWITTER_PASSWORD)
        password_entry.send_keys(Keys.ENTER)
        # Allow time for the page to load.
        sleep(5)
        # Find the tweet field and send the message to the field.
        tweet_field = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div\
            [2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div\
                [1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]\
                    /div/div/div/div')
        message = f"Why does my Internet speed suck so much? I should be getting {TARGET_DOWN} \
            down | {TARGET_UP} UP, and instead im getting {self.down} down | {self.up} up."
        tweet_field.send_keys(message)
        # Find and click on the send tweet button.
        send_tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/d\
            iv/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[\
                2]/div[3]/div/div/div[2]/div[3]')
        send_tweet_button.click()
    # Function to close the bot after the tweet has been published.
    def close(self):
        sleep(5)
        self.driver.quit()
# Instantiate a new bot object.
bot = InternetSpeedTwitterBot(DRIVER_PATH)
# Call the functions of the bot.
bot.get_internet_speed()
bot.tweet()
bot.close()