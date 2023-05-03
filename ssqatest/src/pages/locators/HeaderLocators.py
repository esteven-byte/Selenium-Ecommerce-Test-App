
from selenium.webdriver.common.by import By


class HeaderLocators:

    CART_HEADER_RIGHT = (By.ID, "site-header-cart")
    ITEM_COUNT_HEADER = (By.CSS_SELECTOR, 'ul#site-header-cart span.count')

