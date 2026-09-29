from pages.login_page import Login
from pages.address import ADDRESS
from pages.date_page import DATE
from pages.tractor import TRACTOR

import time
import pytest
@pytest.mark.skip
def test_case(setup):
    L = Login(setup)
    L.pass_mail('anilkumar123@gmail.com')
    L.pass_pwd('Anil@2468')
    time.sleep(2)
    L.submit_button()
    time.sleep(2)
    T = TRACTOR(setup)
    T.tractor_click()
    T.click_tractor()
    T.price_min(2000)
    T.price_max(4000)
    T.click_brand()
    T.select_state()
    T.select_city()
    T.click_apply_filter()
    T.click_book_now()
    time.sleep(2)
    T.select_date()
    T.click_proceed()
    T.click_on_pending()
    T.click_cancel()
    T.click_cancel_confirm()
