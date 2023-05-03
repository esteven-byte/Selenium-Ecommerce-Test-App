from ssqatest.src.pages.locators.MyAccountSignedInLocator import MyAccountSignedInLocator as SignInLocator
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpers.config_helpers import get_base_url
import logging as logger


class MyAccountSignedIn(SignInLocator):

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

    # For registering an account
    def verify_login_logout(self):
        self.sl.check_for_element(SignInLocator.LOGOUT_MY_ACC)
