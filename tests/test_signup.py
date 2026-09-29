from pages.sign_up import SIGNUP
import pytest
import time
from pages.address import ADDRESS
from pages.date_page import DATE
# @pytest.mark.skip
def test_sign(setup):
    S=SIGNUP(setup)
    # setup.get(r'https://agrirental.vercel.app/')
    S.click_get_started()
    S.pass_name('RajkumarSharma')
    S.pass_mail('rajkumarsharma1234@gmail.com')
    S.pass_pass('Rajkumar@2468')
    S.click_create_account()
    S.pass_number('8865408788')
    S.click_continue()
    S.click_farmer()
    S.click_continue_1()
    S.click_continue_2()
    S.pass_address('Shantha nagar,yelahanka,Bengalore')
    S.pass_pin('76859678')
    S.click_complete()


