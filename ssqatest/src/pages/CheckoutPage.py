

from ssqatest.src.pages.locators.CheckoutLocators import CheckoutLocators
from ssqatest.src.SeleniumExtended import SeleniumExtended
from ssqatest.src.helpers.generic_helpers import generate_random_email_and_password


class CheckoutPage(CheckoutLocators):
    def __init__(self, driver):
        self.driver = driver
        self.sl = SeleniumExtended(self.driver)

    def input_billing_first_name(self, first_name=None):
        first_name= first_name if first_name else 'SSQAFname'
        self.sl.wait_and_input_text(self.BILLING_FIRST_NAME, first_name)

    def input_billing_last_name(self, last_name=None):
        last_name = last_name if last_name else 'SSQALname'
        self.sl.wait_and_input_text(self.BILLING_LAST_NAME, last_name)

    def input_billing_address_1(self, address_1=None):
        address_1 = address_1 if address_1 else 'SSQAstreet'
        self.sl.wait_and_input_text(self.BILLING_STREET_NAME,address_1)

    def input_billing_zip_code(self, zipcode=None):
        zipcode = zipcode if zipcode else '5568QA'
        self.sl.wait_and_input_text(self.BILLING_ZIP_CODE, zipcode)

    def input_billing_city(self, city=None):
        city = city if city else 'SSQACity'
        self.sl.wait_and_input_text(self.BILLING_CITY, city)

    def input_billing_phone(self, phone=None):
        phone = phone if phone else '0685556557'
        self.sl.wait_and_input_text(self.BILLING_PHONE, phone)

    def input_billing_email(self, email=None):
        if not email:
            f_email = generate_random_email_and_password()
            email = f_email['email']

        self.sl.wait_and_input_text(self.BILLING_EMAIL, email)

    def fill_in_billing_info(self, f_name=None, l_name=None, address_1=None, zip_code=None, b_city=None, b_phone=None, b_email=None):
        self.input_billing_first_name(first_name=f_name)
        self.input_billing_last_name(last_name=l_name)
        self.input_billing_address_1(address_1=address_1)
        self.input_billing_zip_code(zipcode=zip_code)
        self.input_billing_city(city=b_city)
        self.input_billing_phone(phone=b_phone)
        self.input_billing_email(email=b_email)

    def place_order(self):
        # self.sl.wait_and_click(self.CHECKOUT_PLACE_ORDER)
        self.sl.wait_intercept_click(self.CHECKOUT_PLACE_ORDER)
