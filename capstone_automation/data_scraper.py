from pprint import pprint
from bs4 import BeautifulSoup
import requests


def format_price(price: str):
    return price.split("/")[0].replace("+", "").replace("1 bd", "").strip()


class DataScraper:

    def __init__(self):
        self.data = {}
        html = requests.get('https://appbrewery.github.io/Zillow-Clone/')
        self.soup = BeautifulSoup(html.text, 'html.parser')

    def get_listings(self):
        return self.soup.select("div#grid-search-results > ul > li")

    def get_data(self):
        listings = self.get_listings()

        for i, listing in enumerate(listings[:5], start=1):

            link_el = listing.select_one("a")
            link = link_el.get("href") if link_el else None

            price_el = listing.select_one("span[data-test='property-card-price']")
            price = str(price_el.get_text(strip=True)) if price_el else None
            formatted_price = format_price(price) if price else None

            address_el = listing.select_one("address")
            address = address_el.get_text(strip=True) if address_el else None

            self.data[i] = {
                "link": link,
                "price": formatted_price,
                "address": address,
            }

        return self.data


if __name__ == "__main__":
    scraper = DataScraper()
    scraper.get_data()
    pprint(scraper.data)

