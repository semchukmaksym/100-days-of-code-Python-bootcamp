from api_key import *
import requests
from twilio.rest import Client

API = API_KEY
NEWS_API = NEWS_API_KEY
TWILIO_SID = TWILIO_SID
TWILIO_AUTH_TOKEN = TWILIO_AUTH_TOKEN
TWILIO_PHONE = TWILIO_PHONE
MY_PHONE = MY_PHONE

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
url = "https://www.alphavantage.co/query"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : API
}

stock = requests.get(STOCK_ENDPOINT, params=stock_parameters)

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

data = stock.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday["4. close"]

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diff = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_persentage = (diff / float(yesterday_closing_price)) * 100

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if diff_persentage > 4:
    pass
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.


news_params = {
    "apiKey": NEWS_API_KEY,
    "qInTitle": COMPANY_NAME,
}

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
articles = news_response.json()["articles"]

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

three_articles = articles[:3]

print(three_articles)
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [f"Headline: {article['title']}. \n Brief: {article['description']}" for article in three_articles]
#TODO 9. - Send each article as a separate message via Twilio. 

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

for article in formatted_articles:
    message = client.messages.create(
        body=article,
        from_=TWILIO_PHONE,
        to=MY_PHONE,
    )