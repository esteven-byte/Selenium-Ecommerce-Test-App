
from ssqatest.src.helpers.config_helpers import get_base_url
from ssqatest.src.SeleniumExtended import SeleniumExtended as SLE
from ssqatest.src.pages.locators.HomePageLocators import HomePageLocators


class HomePage(HomePageLocators):

    def __init__(self, driver):
        self.driver = driver

    def go_to_homepage(self):

        home_url = get_base_url()
        self.driver.get(home_url)
        self.SL = SLE(self.driver)

    def add_item_to_cart(self):
        self.SL.wait_and_click(self.ADD_TO_CART)

