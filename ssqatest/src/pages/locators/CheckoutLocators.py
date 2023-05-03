
from selenium.webdriver.common.by import By


class CheckoutLocators:
    BILLING_FIRST_NAME = (By.CSS_SELECTOR, 'input#billing_first_name')
    BILLING_LAST_NAME = (By.CSS_SELECTOR, 'input#billing_last_name')
    BILLING_STREET_NAME = (By.ID, 'billing_address_1')
    BILLING_ZIP_CODE = (By.ID, "billing_postcode")
    BILLING_CITY = (By.ID, 'billing_city')
    BILLING_PHONE = (By.ID, 'billing_phone')
    BILLING_EMAIL = (By.ID, 'billing_email')
    CHECKOUT_PLACE_ORDER = (By.ID, 'place_order')