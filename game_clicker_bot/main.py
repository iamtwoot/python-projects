from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://ozh.github.io/cookieclicker/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

wait = WebDriverWait(driver, 10)

language_div = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="langSelect-EN"]'))
)
language_div.click()


cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')
