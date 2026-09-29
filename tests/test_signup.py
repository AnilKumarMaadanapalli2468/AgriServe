from pages.sign_up import SIGNUP
import pytest
import time
from pages.address import ADDRESS
from pages.date_page import DATE
@pytest.mark.skip
def test_sign(setup):
    S=SIGNUP(setup)
    setup.get(r'https://agrirental.vercel.app/')
    S.click_get_started()
    # S.click_signup()
    S.pass_name('nishanthkumar')
    S.pass_mail('nishanthl123@gmail.com')
    S.pass_pass('Nishanth@2468')
    S.click_create_account()
    S.pass_number('8886708788')
    S.click_continue()
    # F=FARMER(setup)
    # F.click_farmer()
    # time.sleep(3)
    # F.click_continue1()
    # time.sleep(3)
    # Y=YOURSELF(setup)
    # Y.click_continue2()
    # time.sleep(4)
    # A=ADDRESS(setup)
    # A.pass_address('Royal Greens layout,Bengalore')
    # time.sleep(1)
    # A.pass_pin('650090')
    # time.sleep(2)
    # A.click_setup()
    # time.sleep(4)

