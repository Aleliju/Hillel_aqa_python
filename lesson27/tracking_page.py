from selenium.webdriver.common.by import By
from base_page import BasePage

class TrackingPage(BasePage):

    TTN_INPUT = (By.XPATH, "//input[@type='text']")
    SEARCH_BUTTON = (By.XPATH, "//input[@type='submit']")
    INFO_POPUP = (By.XPATH, "//div[@class='first-visit-helper-wrapper d-flex flex-column tracking-desktop']")
    STATUS_TEXT = (By.XPATH, "//div[@class='header__status-text']")

    def enter_ttn(self, ttn):
        self.input_text(self.TTN_INPUT, ttn)

    def click_search(self):
        self.click(self.SEARCH_BUTTON)

    def close_info_popup(self):
        self.click(self.INFO_POPUP)

    def get_status(self):
        return self.get_text(self.STATUS_TEXT)