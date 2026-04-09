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

    data_list = [value for key, value in data.items()]

    yesterday_close = float(data_list[0]["4. close"])
    day_before_yesterday_close = float(data_list[1]["4. close"])

    percent_price_diff = round((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close * 100, 2)
    print(percent_price_diff)
    return percent_price_diff

def get_news(percent_price_diff):
    response = requests.get(news_url, params=news_params)
    response.raise_for_status()
    data = response.json()["articles"]
    send_notification(percent_price_diff, data)


def send_notification(percent_price_diff, news_data):
    symbol_up = "🔺"
    symbol_down = "🔻"
    message = ""
    if percent_price_diff < 0:
        message_title = f'"""\n{STOCK}: {symbol_down}{percent_price_diff}%\n'
    else:
        message_title = f'"""\n{STOCK}: {symbol_up}{percent_price_diff}%\n'

    message += message_title

    for news in news_data:
        message += f'Headline: {news["title"]}\nBrief: {news["description"]}\n--------------------------\n'

    print(message)

calc_price_diff()

price_diff = calc_price_diff()
if abs(price_diff) > 0:
    get_news(price_diff)


