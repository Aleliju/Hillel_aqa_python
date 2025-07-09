import pytest
import allure
from selenium.webdriver import Chrome

from lesson30.garage_page import GaragePage
from lesson30.main_page import MainPage
from lesson30.registration_page import RegistrationPage


@pytest.fixture
def driver():
    driver = Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Positive test")
@allure.story("Valid registration")
def test_registration(driver):
    with allure.step("Open main page"):
        main_page = MainPage(driver)
        main_page.open_main_page("https://guest:welcome2qauto@qauto2.forstudy.space")

    with allure.step("Click sign-up button"):
        main_page.click_sign_up_button()

    with allure.step("Fill in registration details"):
        registration_page = RegistrationPage(driver)
        registration_page.input_signup_name('al')
        registration_page.input_signup_last_name('vas')
        registration_page.input_email("vas", "@ukr.net")
        registration_page.input_password()
        registration_page.input_re_enter_password()

    with allure.step("Submit registration form"):
        registration_page.click_register_button()

    with allure.step("Verify logout button is visible"):
        garage_page = GaragePage(driver)
        assert garage_page.wait_for_logout_button().text == 'Log out'

@allure.feature("Negative test")
@allure.story("Invalid registration")
def test_registration_negative(driver):
    with allure.step("Open main page"):
        main_page = MainPage(driver)
        main_page.open_main_page("https://guest:welcome2qauto@qauto2.forstudy.space")

    with allure.step("Click sign-up button"):
        main_page.click_sign_up_button()

    with allure.step("Fill in registration details"):
        registration_page = RegistrationPage(driver)
        registration_page.input_signup_name('al')
        registration_page.input_signup_last_name('vas')
        registration_page.input_email("vas", "@ukr.net")
        registration_page.input_password()
        registration_page.input_re_enter_password()

    with allure.step("Submit registration form"):
        registration_page.click_register_button()

    with allure.step("Verify incorrect behavior"):
        garage_page = GaragePage(driver)
        assert garage_page.wait_for_logout_button().text == 'Log'

@allure.feature("Positive test")
@allure.story("Check page title")
def test_check_main_page_title(driver):
    with allure.step("Open main page"):
        main_page = MainPage(driver)
        main_page.open_main_page("https://guest:welcome2qauto@qauto2.forstudy.space")

    with allure.step("Verify page title"):
        assert driver.title == "Hillel Qauto"







