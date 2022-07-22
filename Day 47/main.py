#Day 47 of Udemy's 100 Days of Python programming course
import requests
import smtplib
import lxml
from bs4 import BeautifulSoup
from decouple import config

# =============== PRODUCT PRICE FINDING ===============

PRODUCT_URL = config("PRODUCT_URL")

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

response = requests.get(PRODUCT_URL, headers = header)
web_page = response.text

soup = BeautifulSoup(web_page, "lxml")

price = float(soup.find(name = "span", class_ = "a-offscreen").getText().split("$")[1])

item_name = soup.find(id = "productTitle").getText().strip()

# =============== EMAIL ===============

email = config("EMAIL")
password = config("EMAIL_PASSWORD")

target_price = 400.00

if price < target_price:
    with smtplib.SMTP("smtp.gmail.com", port = 587) as connection:
        connection.starttls()
        connection.login(user = email, password = password)
        connection.sendmail(
            from_addr = email,
            to_addrs = email,
            msg = f"Subject: New low price!\n\n{item_name} is on sale for: ${price}.\nBuy here: {PRODUCT_URL}"
        )