
from ssqatest.src.pages.locators.MyAccountSignedOutLocator import MyAccountSignedOutLocator
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpers.config_helpers import get_base_url
import logging as logger


class MyAccountSignedOut(MyAccountSignedOutLocator):

    endpoint = '/my-account/'

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    # To login into your account
    def go_to_my_account(self):
        base_url = get_base_url()
        my_account_url = base_url + self.endpoint
        logger.info(f"Going to: {my_account_url}")
        self.driver.get(my_account_url)

    def input_login_username(self, username):
        self.sl.wait_and_input_text(self.LOGIN_USER_NAME, username)

    def input_login_password(self, password):
        self.sl.wait_and_input_text(self.LOGIN_PASSWORD, password)

    def click_login_button(self):
        logger.info(f"Debugger: Click login button")
        self.sl.wait_and_click(self.LOGIN_BTN)

    # For registering an account
    def wait_until_error_is_displayed(self, exp_err):
        return self.sl.wait_until_element_text(self.WOO_ERROR, exp_err)

    def input_register_email(self, username):
        self.sl.wait_and_input_text(self.REGISTER_EMAIL, username)

    def input_register_password(self, password):
        self.sl.wait_and_input_text(self.REGISTER_PASSWORD, password)

    def click_register_button(self):
        logger.info(f"Debugger: Click login button")
        self.sl.wait_and_click(self.REGISTER_BTN)
