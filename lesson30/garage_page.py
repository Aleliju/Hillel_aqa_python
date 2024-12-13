from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GaragePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_logout_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//a[@class='btn btn-link text-danger btn-sidebar sidebar_btn']"))
        )