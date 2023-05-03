
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.pages.locators.CartPageLocators import CartPageLocators
import time


class CartPage(CartPageLocators):

    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def go_to_cart_page(self):
        pass

    def get_all_product_names_in_cart(self):
        product_name_elements = self.sl.wait_and_get_elements(self.CART_ITEM_NAMES)
        product_names = [i.text for i in product_name_elements]
        return product_names

    def apply_coupon(self, coupon_code):
        self.sl.wait_and_input_text(self.CART_COUPON_INPUT, coupon_code)
        self.sl.wait_and_click(self.CART_COUPON_BTTN)
        message = self.get_coupon_status()
        pass_alert = 'Coupon code applied successfully.'
        assert message == pass_alert, f"The coupon {coupon_code} is not successful, check you're code"
        # self.sl.check_for_element(self.CART_COUPON_ACCEPT)

        self.sl.wait_until_element_text(self.CART_TOTAL, '€ 0,00')

    def get_coupon_status(self):
        coupon_alert = self.sl.wait_for_text(self.CART_SUCCESS_ALERT)
        return coupon_alert

    def click_on_proceed_to_checkout(self):
        # self.sl.wait_and_click(self.CART_CHECKOUT_BTTN)
        self.sl.wait_intercept_click(self.CART_CHECKOUT_BTTN)

