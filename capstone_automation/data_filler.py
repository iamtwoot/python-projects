import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

GOOGLE_FORM_LINK = "https://forms.gle/24THopc99YuMma4i9"

class DataFiller:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 3)

    def fill_the_form(self, data):
        for i, listing in data.items():
            self.driver.get(GOOGLE_FORM_LINK)

            address_el = self.driver.find_element(
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input',
            )
            address_input = self.wait.until(EC.element_to_be_clickable(address_el))

            price_el = self.driver.find_element(
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
            )
            price_input = self.wait.until(EC.element_to_be_clickable(price_el))


            link_el = self.driver.find_element(
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input',
            )
            link_input = self.wait.until(EC.element_to_be_clickable(link_el))

            address_input.send_keys(listing["address"])
            price_input.send_keys(listing["price"])
            link_input.send_keys(listing["link"])

            submit_btn = self.driver.find_element(
                By.XPATH,
                '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span',
            )
            submit_btn.click()

            time.sleep(2)

if __name__ == "__main__":
    filler = DataFiller()
    filler.fill_the_form()


