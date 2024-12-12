from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def open_main_page(self, url):
        self.driver.get(url)

    def click_sign_up_button(self):
        self.driver.find_element(By.XPATH, "//button[@class = 'hero-descriptor_btn btn btn-primary']").click()
