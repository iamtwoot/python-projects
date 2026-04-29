from data_scraper import DataScraper
from data_filler import DataFiller

scraper = DataScraper()
filler = DataFiller()

data = scraper.get_data()
filler.fill_the_form(data)