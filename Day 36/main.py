# Day 36 of Udemy's 100 Days of Python programming course
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = "ACCOUNT SID HERE"
auth_token = "AUTH TOKEN HERE"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_url = "https://www.alphavantage.co/query"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "API KEY HERE"
}
stock_response = requests.get(url = stock_url, params = stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]


difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

up_down = None

if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
dif_percent = round((difference / float(yesterday_closing_price)) * 100)

if dif_percent > 5:
    print("Get News")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

news_url = "https://newsapi.org/v2/everything"
news_params = {
    "q": "tesla",
    "from": "",
    "sortBy": "publishedAt",
    "apiKey": "API KEY HERE",
    "language": "en",
    "qInTitle": "title search"
    
}
news_response = requests.get(url = news_url, params = news_params)
news_response.raise_for_status()
news_data = news_response.json()["articles"]

three_articles = news_data[:3]



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
formatted_articles = [f"{STOCK}: {up_down}{dif_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

print(formatted_articles)

#Optional: Format the SMS message like this: 
client = Client(account_sid, auth_token)
for article in formatted_articles:
    message = client.messages.create(
        body = article,
        from_="FROM NUMBER HERE",
        to="TO NUMBER HERE"

    )


