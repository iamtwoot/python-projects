import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.raise_for_status()

html = response.text

soup = BeautifulSoup(html, 'html.parser')

titles = soup.select("div.article-title-description h3.title")
titles_reverse = titles[::-1]

with open("movies.txt", "w", encoding="UTF-8") as file:
    for title in titles_reverse:
        file.write(title.text + "\n")


