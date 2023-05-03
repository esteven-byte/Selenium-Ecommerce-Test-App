
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, \
    ElementClickInterceptedException, ElementNotInteractableException
import time

class SeleniumExtended:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 15

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            # WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).click()
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()
        except StaleElementReferenceException:
            time.sleep(2)
            # WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).click()
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()

    def wait_for_text(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        tx = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).text
        return tx

    def wait_until_element_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        tx = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

        return tx

    def check_for_element(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_and_get_elements(self, locator, timeout=None, err=None):
        timeout = timeout if timeout else self.default_timeout
        err = err if err else f"Unable to find elements located by '{locator}," \
                              f"after timeout of {timeout}"
        try:
            item = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise TimeoutException(err)
        return item

    def wait_intercept_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator)).click()
        except ElementClickInterceptedException:
            time.sleep(2)
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).click()
        except StaleElementReferenceException:
            time.sleep(2)
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).click()






