from pages.login_page import Login
from pages.address import ADDRESS
from pages.date_page import DATE
from pages.tractor import TRACTOR
from pages.sign_up import SIGNUP
import allure

import time
import pytest
#pytest.mark.skip
@allure.title('Verify tractor booking flow')
@allure.feature("Tractor")
@allure.story("User books and cancels a tractor")

def test_case(setup):
    with allure.step('Get started'):
        S=SIGNUP(setup)
        S.click_get_started()
    with allure.step('Click on Sign in'):
        L = Login(setup)
        L.click_signin()
    with allure.step("Login to the application"):
        L.pass_mail('anilkumar123@gmail.com')
        L.pass_pwd('Anil@2468')
        time.sleep(1)
        L.submit_button()
        time.sleep(2)
    with allure.step('Open tractor section'):
        T = TRACTOR(setup)
        T.tractor_click()
    with allure.step('Select tractor'):
        T.click_tractor()
    with allure.step('Enter minimum price'):
        T.price_min(2000)
    with allure.step('Enter maximum price'):
        T.price_max(4000)
    with allure.step('Select brand'):
        T.click_brand()
    with allure.step('Select state'):
        T.select_state()
    with allure.step('Select city'):
        T.select_city()
    with allure.step('Apply filters'):
        T.click_apply_filter()
    with allure.step('Click book now'):
        T.click_book_now()
        time.sleep(2)
    with allure.step('Select booking date'):
        T.select_date()
    with allure.step('Proceed with booking'):
        T.click_proceed()
    with allure.step('open pending bookings'):
        T.click_on_pending()
    with allure.step('click cancel'):
        T.click_cancel()
    with allure.step('Confirm cancellation'):
        T.click_cancel_confirm()
