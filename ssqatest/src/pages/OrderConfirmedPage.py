

from ssqatest.src.pages.locators.OrderConfirmedLocators import OrderConfirmedLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended


class OrderConfirmed(OrderConfirmedLocators):

    def __init__(self, driver):
        assert driver, "driver argument for OrderConfirmed object must be given"
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def check_order_confirmation(self):
        self.sl.wait_until_element_text(self.ORDER_TITLE, "Order received")

    def get_order_number(self):
        return self.sl.wait_for_text(self.ORDER_NUMBER)

