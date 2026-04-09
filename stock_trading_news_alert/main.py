import requests
from datetime import date, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Alpha (stocks) data
ALPHA_API_KEY = "AM4CYEHS3I1KGJ8H"
alpha_url = "https://www.alphavantage.co/query?"
alpha_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_API_KEY,
}

# News data
NEWS_API_KEY = "56cd6bf338af4effbfa2cf3bd7d2afa7"
news_url = "https://newsapi.org/v2/everything?"
news_params = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "pageSize": 3,
}


def calc_price_diff():

    response = requests.get(alpha_url, params=alpha_params)
    response.raise_for_status()
    data = response.json()["Time Series (Daily)"]

    yesterday = date.today() - timedelta(days=1)
    yesterday_str = yesterday.strftime("%Y-%m-%d")

    day_before_yesterday = date.today() - timedelta(days=2)
    day_before_yesterday_str = day_before_yesterday.strftime("%Y-%m-%d")

    yesterday_close = float(data[yesterday_str]["4. close"])
    day_before_yesterday_close = float(data[day_before_yesterday_str]["4. close"])

    percent_price_diff = round((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close * 100, 2)
    print(percent_price_diff)
    return percent_price_diff

def get_news():
    response = requests.get(news_url, params=news_params)
    response.raise_for_status()
    data = response.json()["articles"]
    for news in data:
        print(news["title"])


if abs(calc_price_diff()) > 0:
    get_news()



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

