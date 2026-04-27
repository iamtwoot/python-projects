import os
from selenium import webdriver

GYM_URL = "https://appbrewery.github.io/gym/"
ACCOUNT_EMAIL = "daniil@test.ru"
ACCOUNT_PASSWORD = "g45yg45g45g34g4efdhgaJHGV"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)

driver.get(GYM_URL)
