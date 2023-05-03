
from selenium.webdriver.common.by import By


class OrderConfirmedLocators:

    ORDER_TITLE = (By.CLASS_NAME, 'entry-title')
    ORDER_NUMBER = (By.CSS_SELECTOR, 'li.order strong')
