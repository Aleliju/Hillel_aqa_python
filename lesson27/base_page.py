from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, xpath, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(xpath))

    def click(self, xpath):
        element = self.wait_for_element(xpath)
        element.click()

    def input_text(self, xpath, text):
        element = self.wait_for_element(xpath)
        element.clear()
        element.send_keys(text)

    def get_text(self, xpath):
        element = self.wait_for_element(xpath)
        return element.text