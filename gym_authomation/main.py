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

next_tue_classes = driver.find_element(By.CSS_SELECTOR, "div[id*='tue']")
date = next_tue_classes.find_element(By.CSS_SELECTOR, "h2").text

class_to_book = next_tue_classes.find_element(By.CSS_SELECTOR, "div[id*='1800']")
class_name = class_to_book.find_element(By.CSS_SELECTOR, "h3").text

book_btn = class_to_book.find_element(By.CSS_SELECTOR, "button[id^='book-']")

booked_count = 0
waitlist_count = 0
already_booked_count = 0

if book_btn.text == "Booked":
    already_booked_count += 1
    print(f"✓ Already booked: {class_name} on {date}")
elif book_btn.text == "Waitlisted":
    already_booked_count += 1
    print(f"✓ Already on waitlist: {class_name} on {date}")
elif book_btn.text == "Join Waitlist":
    waitlist_count += 1
    book_btn.click()
    print(f"✓ Joined waitlist for: {class_name} on {date}")
else:
    booked_count += 1
    book_btn.click()
    print(f"✓ Booked: {class_name} on {date}")

print("\n--- BOOKING SUMMARY ---")
print(f"Classes booked: {booked_count}")
print(f"Waitlists joined {waitlist_count}")
print(f"Already booked/waitlisted: {already_booked_count}")
print(f"Total Tuesday 6pm classes processed: {booked_count + waitlist_count + already_booked_count}")