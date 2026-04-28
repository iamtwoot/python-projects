import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

GYM_URL = "https://appbrewery.github.io/gym/"
ACCOUNT_EMAIL = "daniil@test.ru"
ACCOUNT_PASSWORD = "g45yg45g45g34g4efdhgaJHGV"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 10)

driver.get(GYM_URL)

login = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#login-button"))
)
login.click()

email_input = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#email-input"))
)
email_input.send_keys(ACCOUNT_EMAIL)

password_input = driver.find_element(By.CSS_SELECTOR, "#password-input")
password_input.send_keys(ACCOUNT_PASSWORD)

login_button = driver.find_element(By.CSS_SELECTOR, "#submit-button")
login_button.click()

wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))
