from selenium.webdriver.common.by import By
from datetime import datetime

password = 'Qwerty123'

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def signup_name_input_field(self):
        signup_name_input = self.driver.find_element(By.XPATH, "//input[@id= 'signupName']")
        signup_name = 'al'
        signup_name_input.clear()
        signup_name_input.send_keys(signup_name)

    def signup_last_name_input_field(self):
        signup_last_name_input = self.driver.find_element(By.XPATH, "//input[@id= 'signupLastName']")
        signup_last_name = 'vas'
        signup_last_name_input.clear()
        signup_last_name_input.send_keys(signup_last_name)

    def email_input_field(self):
        base_email = "vas"
        domain = "@ukr.net"
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        unique_email = f'{base_email}{timestamp}{domain}'
        email_input = self.driver.find_element(By.XPATH, "//input[@id= 'signupEmail']")
        email_input.clear()
        email_input.send_keys(unique_email)

    def password_input_field(self):
        password_input = self.driver.find_element(By.XPATH, "//input[@id= 'signupPassword']")
        password_input.clear()
        password_input.send_keys(password)

    def re_enter_password_input(self):
        re_enter_password_input = self.driver.find_element(By.XPATH, "//input[@id= 'signupRepeatPassword']")
        re_enter_password_input.clear()
        re_enter_password_input.send_keys(password)

    def register_button(self):
        register_button = self.driver.find_element(By.XPATH, "//button[@class= 'btn btn-primary']").click()
