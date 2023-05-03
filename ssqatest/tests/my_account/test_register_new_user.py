
import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.pages.MyAccountSignedIn import MyAccountSignedIn
from ssqatest.src.helpers.generic_helpers import generate_random_email_and_password as email_password


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.tcid13
    def test_rester_valid_new_user(self):
        my_account_o = MyAccountSignedOut(self.driver)
        my_account_i = MyAccountSignedIn(self.driver)
        # go to my account
        my_account_o.go_to_my_account()
        # fill in email
        reg_email = email_password().get("email")
        my_account_o.input_register_email(reg_email)
        # fill in password
        my_account_o.input_register_password("incontrol56789")
        # click register
        my_account_o.click_register_button()
        # verify user is registered
        my_account_i.verify_login_logout()


        # import pdb;
        # pdb.set_trace()

