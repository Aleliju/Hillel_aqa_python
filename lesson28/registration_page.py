from selenium.webdriver.common.by import By
from datetime import datetime
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
try:
    password = config['credentials']['password']
except KeyError:
    raise KeyError("Missing 'password' in 'credentials' section of config.ini")


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def input_signup_name(self, signup_name):
        signup_name_input = self.driver.find_element(By.XPATH, "//input[@id= 'signupName']")
        signup_name_input.clear()
        signup_name_input.send_keys(signup_name)

    def input_signup_last_name(self, signup_last_name):
        signup_last_name_input = self.driver.find_element(By.XPATH, "//input[@id= 'signupLastName']")
        signup_last_name_input.clear()
        signup_last_name_input.send_keys(signup_last_name)

    def input_email(self, base_email, domain):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        unique_email = f'{base_email}{timestamp}{domain}'
        email_input = self.driver.find_element(By.XPATH, "//input[@id= 'signupEmail']")
        email_input.clear()
        email_input.send_keys(unique_email)

    def input_password(self, password):
        password_input = self.driver.find_element(By.XPATH, "//input[@id= 'signupPassword']")
        password_input.clear()
        password_input.send_keys(password)

    def input_re_enter_password(self, password):
        re_enter_password_input = self.driver.find_element(By.XPATH, "//input[@id= 'signupRepeatPassword']")
        re_enter_password_input.clear()
        re_enter_password_input.send_keys(password)

    def click_register_button(self):
        self.driver.find_element(By.XPATH, "//button[@class= 'btn btn-primary']").click()
