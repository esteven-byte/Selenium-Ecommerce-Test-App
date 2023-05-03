
from selenium.webdriver.common.by import By


class CartPageLocators:

    CART_ITEM_NAMES = (By.CSS_SELECTOR, 'tr.cart_item td.product-name')
    CART_COUPON_INPUT = (By.CSS_SELECTOR, 'input#coupon_code')
    CART_COUPON_BTTN = (By.CSS_SELECTOR, 'button[name="apply_coupon"]')
    CART_SUCCESS_ALERT = (By.CSS_SELECTOR, 'div.woocommerce-message')
    CART_CHECKOUT_BTTN = (By.CSS_SELECTOR, "a.checkout-button")
    CART_TOTAL = (By.CSS_SELECTOR, 'tr.order-total span.woocommerce-Price-amount')
