import time
from datetime import date

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from datetime import date, timedelta
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class DATE:

    date = '//button[@aria-label="Saturday, September 26th, 2026"]'
    confirm = "//button[text()='Confirm Booking']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click_date(self):
        day=self.wait.until(EC.presence_of_element_located(('xpath',self.date)))
        ActionChains(self.driver).scroll_to_element(day).perform()
        day.click()
        time.sleep(3)


    def click_confirm(self):
        conf=self.wait.until(EC.presence_of_element_located(('xpath', self.confirm)))
        conf.click()
        time.sleep(3)