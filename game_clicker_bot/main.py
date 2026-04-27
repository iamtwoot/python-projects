import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://ozh.github.io/cookieclicker/"
CHECK_INTERVAL = 5
GAME_LONG = 300

def check_for_upgrades():
    available_upgrades = driver.find_elements(By.CSS_SELECTOR, "#products .enabled")
    latest_upgrade = available_upgrades[-1]
    latest_upgrade.click()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

wait = WebDriverWait(driver, 10)

language_div = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="langSelect-EN"]'))
)
language_div.click()

time.sleep(5)

cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')

start_time = time.time()
next_check = start_time + CHECK_INTERVAL
stop_time = time.time() + GAME_LONG

game_is_on = True

while game_is_on:
    cookie.click()

    if time.time() >= next_check:
        check_for_upgrades()
        next_check += CHECK_INTERVAL

    if time.time() >= stop_time:
        game_is_on = False

cookies_per_second = driver.find_element(By.XPATH, '//*[@id="cookiesPerSecond"]')
print(f"cookies/second: {cookies_per_second.text}")
