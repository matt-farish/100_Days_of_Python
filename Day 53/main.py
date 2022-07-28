#Day 53 of Udemy's 100 Days of Python programming course
from time import sleep
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdwxt5ahRE4KrKsG1gTW9oW6BF95NMzbsR2DkFZUlcKZ4ZcTw/viewform?usp=sf_link"
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

response = requests.get(ZILLOW_URL, headers = header)

data = response.text
soup = BeautifulSoup(data, "html.parser")

links = soup.select(".list-card-top a")

url_list = []
for link in links:
    href = link["href"]
    if "http" not in href:
        url_list.append(f"https://www.zillow.com{href}")
    else:
        url_list.append(href)

all_address_elements = soup.select(".list-card-info address")
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]

all_price_elements = soup.select(".list-card-heading")
for element in all_price_elements:
    print(element.select(".list-card-price")[0].contents)

# all_prices = []
# for element in all_price_elements:
#     try:
#         price = element.select(".list-card-price")[0].contents[0]
#     except IndexError:
#         print("Multiple listings for the card")
#         price = element.select(".list-card-details li")[0].contents[0]
#     finally:
#         all_prices.append(price)



# driver_path = Service("C:\Development\chromedriver.exe")
# driver = webdriver.Chrome(service = driver_path)

# for i in range(len(url_list)):
#     driver.get(FORM_URL)

#     sleep(3)

#     address = driver.find_element(By.XPATH, 
#         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     price = driver.find_element(By.XPATH,
#         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     link = driver.find_element(By.XPATH, 
#         '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
#     submit_button = driver.find_element(By.XPATH, 
#         '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    
#     address.send_keys(all_addresses[i])
#     price.send_keys(all_prices[i])
#     link.send_keys(url_list[i])
#     submit_button.click()