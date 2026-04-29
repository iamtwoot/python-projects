from selenium import webdriver

GOOGLE_FORM_LINK = "https://forms.gle/24THopc99YuMma4i9"

class DataFiller:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)



