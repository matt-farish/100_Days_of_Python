#Day 50 of Udemy's 100 Days of Python programming course
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from decouple import config

# Create the driver and have it open the tinder homepage.
driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service = driver_path)
driver.get("https://tinder.com/")

# Allow the page to fully load.
sleep(3)

# Find and click on the login button.
login_button = driver.find_element(By.CSS_SELECTOR, ".H\(40px\) .button")
login_button.click()

# Allow the page to fully load.
sleep(2)

# Find and click on the login with Facebook button.
login_w_facebook = driver.find_element(By.XPATH, '//*[@id="t-831228276"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
login_w_facebook.click()

# Allow the page to fully load.
sleep(3)

# Allocate the windows in view to variables, and switch to the Facebook login window.
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# Assign phone number and password variables from .env file.
PHONE = config("PHONE")
PASSWORD = config("PASSWORD")

# Find the username entry field and enter phone number.
email_entry = driver.find_element(By.XPATH, '//*[@id="email"]')
email_entry.send_keys(PHONE)

# Find the password entry field and enter the stored password value.
password_entry = driver.find_element(By.XPATH, '//*[@id="pass"]')
password_entry.send_keys(PASSWORD)
password_entry.send_keys(Keys.ENTER)

# Allow for time to accept 2FA request.
sleep(15)

# Switch back to the Tinder window once logged in.
driver.switch_to.window(base_window)

# Allow the page to fully load.
sleep(5)

# Find and click on the location services button
location_allow = driver.find_element(By.XPATH, '//*[@id="t-831228276"]/div/div/div/div/div[3]/button[1]')
location_allow.click()

# Allow the page to fully load.
sleep(5)

# Find and click on the notifications button
notifications_allow = driver.find_element(By.XPATH, '//*[@id="t-831228276"]/div/div/div/div/div[3]/button[1]')
notifications_allow.click()

# Allow the page to fully load.
sleep(5)

# Find and click on the deny cookies button.
cookies_decline = driver.find_element(By.XPATH, '//*[@id="t897152800"]/div/div[2]/div/div/div[1]/div[2]/button')
cookies_decline.click()

# Variables for both the like and dislike buttons.
dislike_button = driver.find_element(By.XPATH, '//*[@id="t897152800"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button')
like_button = driver.find_element(By.XPATH, '//*[@id="t897152800"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')

# Being limited to 100 likes per day on the free version of Tinder, only attempt to like 100 times.
for i in range(100):
    # Allow for a one second pause between likes, to avoid being considered a bot account.
    sleep(1)
    # Click the like button.
    try:
        print("called")
        like_button.click()

    # If a match occurs, click on the match popup.
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        # If loading new people, wait for person cards to return.
        except NoSuchElementException:
            sleep(2)

# Once 100 likes have been sent, exit.
driver.quit()