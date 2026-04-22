from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_tag = soup.select("span.titleline a")

article_text = article_tag[0].text
article_link = article_tag[0].get("href")
article_upvote = soup.select("span.score")[0].text
