import pytest
from selenium.webdriver import Chrome

from lesson28.garage_page import GaragePage
from lesson28.main_page import MainPage
from lesson28.registration_page import RegistrationPage


@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_registration(driver):
    main_page = MainPage(driver)
    registration_page = RegistrationPage(driver)
    garage_page = GaragePage(driver)

    main_page.open_main_page("https://guest:welcome2qauto@qauto2.forstudy.space")
    main_page.sign_up_button()

    registration_page.signup_name_input_field()
    registration_page.signup_last_name_input_field()
    registration_page.email_input_field()
    registration_page.password_input_field()
    registration_page.re_enter_password_input()
    registration_page.register_button()

    assert garage_page.wait_for_logout_button().text == 'Log out'






