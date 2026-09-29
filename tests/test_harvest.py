from pages.harvest_page import HARVESTER
import pytest

from pages.login_page import Login
from pages.tractor import TRACTOR


# @pytest.mark.skip
def test_harv(setup):
    H=HARVESTER(setup)
    L = Login(setup)
    L.pass_mail('anilkumar123@gmail.com')
    L.pass_pwd('Anil@2468')
    L.submit_button()
    H.click_harvester()
    H.price_min(1000)
    H.price_max(5000)
    H.click_brand()
    H.select_state()
    H.select_city()
    H.click_apply_filter()
    H.click_jhonDhere()
    H.click_harv()
    H.click_book_now()
    H.select_date()
    H.click_proceed()
    H.click_on_pending()
    H.click_cancel()
    H.click_cancel_confirm()
