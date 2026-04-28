import os
import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

GYM_URL = "https://appbrewery.github.io/gym/"
ACCOUNT_EMAIL = "daniil@test.ru"
ACCOUNT_PASSWORD = "g45yg45g45g34g4efdhgaJHGV"

def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)

def login():
    login_btn = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#login-button"))
    )
    login_btn.click()

    email_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#email-input"))
    )
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = driver.find_element(By.CSS_SELECTOR, "#password-input")
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    login_button = driver.find_element(By.CSS_SELECTOR, "#submit-button")
    login_button.click()

    wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, 2)

retry(login, description="login")
# ---------------------------- FIND AND BOOK CLASSES ---------------------------------- #
booked_count = 0
waitlist_count = 0
already_booked_count = 0

new_bookings = []
new_waitlists = []

# ALL TUESDAY CLASSES
next_tue_classes = driver.find_element(By.CSS_SELECTOR, "div[id*='tue']")
classes_to_book = next_tue_classes.find_elements(By.CSS_SELECTOR, "div[id^='class-card']")

# 6 PM THURSDAY CLASSES
next_thu_classes = driver.find_element(By.CSS_SELECTOR, "div[id*='thu']")
classes_to_book.append(next_thu_classes.find_element(By.CSS_SELECTOR, "div[id*='1800']"))

for class_to_book in classes_to_book:
    class_name = class_to_book.find_element(By.CSS_SELECTOR, "h3").text
    class_date = class_to_book.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group')]//h2").text
    try:
        formatted_class_date = class_date.split("(")[1].split(")")[0]
    except IndexError:
        formatted_class_date = class_date
    book_btn = class_to_book.find_element(By.CSS_SELECTOR, "button[id^='book-']")

    if book_btn.text == "Booked":
        already_booked_count += 1
        print(f"✓ Already booked: {class_name} on {formatted_class_date}")
    elif book_btn.text == "Waitlisted":
        already_booked_count += 1
        print(f"✓ Already on waitlist: {class_name} on {formatted_class_date}")
    elif book_btn.text == "Join Waitlist":
        waitlist_count += 1
        book_btn.click()
        print(f"✓ Joined waitlist for: {class_name} on {formatted_class_date}")
        new_waitlists.append(f"{class_name} on {formatted_class_date}")
    else:
        booked_count += 1
        book_btn.click()
        print(f"✓ Booked: {class_name} on {formatted_class_date}")
        new_bookings.append(f"{class_name} on {formatted_class_date}")

    time.sleep(0.5)

# ------------------- CHECK MY BOOKINGS ------------------------------- #
total_booked = len(new_bookings) + len(new_waitlists)
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---")
print("\n--- VERIFYING ON MY BOOKING PAGE ---")

bookings_link = driver.find_element(By.CSS_SELECTOR, "a#my-bookings-link")
bookings_link.click()

wait.until(EC.presence_of_element_located((By.ID, "my-bookings-page")))

confirmed_bookings = driver.find_elements(By.XPATH, "//div[contains(@id, 'booking-card')]")
confirmed_waitlists = driver.find_elements(By.XPATH, "//div[contains(@id, 'waitlist-card')]")
verified_count = len(confirmed_bookings) + len(confirmed_waitlists)

print("\n--- VERIFICATION RESULT ---")
print(f"Expected bookings: {total_booked}")
print(f"Verified bookings: {verified_count}")

if verified_count == total_booked:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")

print("\n--- BOOKING SUMMARY ---")
print(f"Classes booked: {booked_count}")
print(f"Waitlists joined: {waitlist_count}")
print(f"Already booked/waitlisted: {already_booked_count}")
print(f"Total Tuesday 6pm classes processed: {booked_count + waitlist_count + already_booked_count}")

print(f"\n--- DETAILED CLASS LIST ---")
if new_bookings or new_waitlists:
    for new_booking in new_bookings:
        print(f"• [New Booking] {new_booking}")
    for new_waitlist in new_waitlists:
        print(f"• [New Waitlist] {new_waitlist}")
else:
    print("No [new bookings] or [new waitlists]")
