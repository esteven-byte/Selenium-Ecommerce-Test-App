
import time
import pytest
import pdb
from ssqatest.src.pages.HomePage import HomePage
from ssqatest.src.pages.Header import Header
from ssqatest.src.pages.CartPage import CartPage
from ssqatest.src.pages.CheckoutPage import CheckoutPage
from ssqatest.src.configs.generic_configs import GenericConfigs
from ssqatest.src.pages.OrderConfirmedPage import OrderConfirmed
from ssqatest.src.helpers.database_helper import get_order_from_db_by_order_no


@pytest.mark.usefixtures('init_driver')
class TestEndToEndCheckoutGuest:
    @pytest.mark.tcid33
    def test_end_to_end_checkout_guest_user(self):
        home_p = HomePage(self.driver)
        header = Header(self.driver)
        cart_p = CartPage(self.driver)
        checkout_p = CheckoutPage(self.driver)
        order_p = OrderConfirmed(self.driver)
        # got to home page

        home_p.go_to_homepage()

        # add1 item to cart
        home_p.add_item_to_cart()

        # go to cart
        header.wait_for_cart_items(1)
        header.click_cart_on_right_header()
        cart_item_names = cart_p.get_all_product_names_in_cart()

        # apply free coupon
        coupon_code = GenericConfigs.FREE_COUPON
        # cart_p.apply_coupon('abc')
        cart_p.apply_coupon(coupon_code)

        # go to check out
        # pdb.set_trace()
        cart_p.click_on_proceed_to_checkout()

        #fill in form
        checkout_p.fill_in_billing_info()

        # click on place order
        checkout_p.place_order()

        #verify order is received
        order_p.check_order_confirmation()

        # verify order is recorded in db (via SQL or via API)
        order_number = order_p.get_order_number()
        db_order = get_order_from_db_by_order_no(order_number)
        assert db_order, f"After creating order with FE, not found in DB" \
                        f"Order no: {order_number}"
        print("")
        print('****************')
        print('PASS')
        print('****************')
        # pdb.set_trace()