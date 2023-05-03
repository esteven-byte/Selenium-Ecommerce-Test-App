
import pytest
from ssqatest.src.pages.MyAccountSignedOut import MyAccountSignedOut
from ssqatest.src.helpers.generic_helpers import generate_random_email_and_password as email_password


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid12
    def test_login_none_existing_user(self):
        my_account = MyAccountSignedOut(self.driver)
        # go to my account
        # assert my_account == 'yeah', 'my account does not match'
        my_account.go_to_my_account()
        # type username
        random_email = email_password().get('email')
        my_account.input_login_username(random_email)
        # type password
        my_account.input_login_password('100%real')
        # click login
        my_account.click_login_button()
        # verify error message
        msg_error = f'Unknown email address. Check again or try your username.'
        my_account.wait_until_error_is_displayed(msg_error)
        # import pdb;
        # pdb.set_trace()



