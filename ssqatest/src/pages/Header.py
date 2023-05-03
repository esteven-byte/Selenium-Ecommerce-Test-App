
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.HeaderLocators import HeaderLocators


class Header(HeaderLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def wait_for_cart_items(self, count=1):
        if type(count) != int:
            raise Exception("argument 'count' must be object type integer")
        elif count > 1:
            cart_items = str(count) + " items"
        else:
            cart_items = str(count) + " item"

        self.sl.wait_until_element_text(self.ITEM_COUNT_HEADER, cart_items)

    def click_cart_on_right_header(self):
        self.sl.wait_and_click(self.CART_HEADER_RIGHT)
