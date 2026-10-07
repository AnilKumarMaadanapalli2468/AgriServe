import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TRACTOR:
    tractor="//button[text()='Tractors']"
    price_minimum = '(//input[@class="flex h-10 w-full rounded-lg border border-gray-700 bg-[#252525] pl-7 pr-3 text-sm text-white placeholder:text-gray-600 focus:border-cyan-500 focus:outline-none focus:ring-1 focus:ring-cyan-500"])[1]'
    price_maximum = '(//input[@class="flex h-10 w-full rounded-lg border border-gray-700 bg-[#252525] pl-7 pr-3 text-sm text-white placeholder:text-gray-600 focus:border-cyan-500 focus:outline-none focus:ring-1 focus:ring-cyan-500"])[2]'
    brand = "//span[text()='Mahindra']"
    state = '//select[@class="w-full appearance-none rounded-lg border border-gray-700 bg-[#252525] px-4 py-2.5 text-white focus:border-cyan-500 focus:outline-none focus:ring-1 focus:ring-cyan-500"]'
    city = '//select[@class="w-full appearance-none rounded-lg border border-gray-700 bg-[#252525] px-4 py-2.5 text-white transition-opacity focus:border-cyan-500 focus:outline-none focus:ring-1 focus:ring-cyan-500 disabled:cursor-not-allowed disabled:opacity-50"]'
    apply_filter = "//button[text()='Apply Filters']"
    book_now='(//button[@class="flex flex-1 items-center justify-center gap-2 rounded-full bg-cyan-500 py-2.5 text-sm font-semibold text-white transition-colors hover:bg-cyan-400"])[1]'
    date_select='//button[@aria-label="Thursday, October 8th, 2026"]'
    proceed="(//button[text()='Proceed to Pay'])[2]"
    click_pending='(//div[@class="flex gap-4"])[1]'
    cancel='//button[@class="inline-flex items-center justify-center gap-2 whitespace-nowrap rounded-lg text-sm font-medium focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-[#3b82f6] focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0 border h-10 px-4 py-2 w-full cursor-pointer border-red-500/30 bg-red-500/5 text-red-400 transition-all duration-200 hover:border-red-500 hover:bg-red-500/10"]'
    confirm_cancel="//button[text()='Confirm Cancel']"
    tractor_1="//span[text()='Tractor']"
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,20)
    def tractor_click(self):
        self.driver.find_element('xpath',self.tractor_1).click()
        time.sleep(2)

    def click_tractor(self):
        self.driver.find_element('xpath',self.tractor).click()
        time.sleep(2)
    def price_min(self,min_price):
        self.driver.find_element('xpath',self.price_minimum).send_keys(min_price)
        time.sleep(2)
    def price_max(self, max_price):
        self.driver.find_element('xpath', self.price_maximum).send_keys(max_price)
        time.sleep(2)
    def click_brand(self):
        brand_ele=self.wait.until(EC.element_to_be_clickable(('xpath',self.brand)))
        ActionChains(self.driver).scroll_to_element(brand_ele).perform()
        brand_ele.click()

        time.sleep(2)

    def select_state(self):
        state_ele=self.driver.find_element('xpath',self.state)
        ob=Select(state_ele)
        ob.select_by_visible_text('Madhya Pradesh')
        time.sleep(2)
    def select_city(self):
        city_ele=self.driver.find_element('xpath',self.city)
        ob=Select(city_ele)
        ob.select_by_visible_text('Chhindwara')
        time.sleep(2)

    def click_apply_filter(self):
        filter_btn=self.wait.until(EC.element_to_be_clickable(('xpath',self.apply_filter)))
        filter_btn.click()
        time.sleep(4)
    def click_book_now(self):
        self.driver.find_element('xpath',self.book_now).click()
        time.sleep(2)
    def select_date(self):
        date_ele=self.wait.until(EC.element_to_be_clickable(('xpath',self.date_select)))
        ActionChains(self.driver).scroll_to_element(date_ele).perform()
        date_ele.click()

        time.sleep(2)
    def click_proceed(self):
        proceed_ele=self.wait.until(EC.element_to_be_clickable(('xpath',self.proceed)))
        proceed_ele.click()
        time.sleep(1)
    def click_on_pending(self):
        self.driver.find_element('xpath',self.click_pending).click()
        time.sleep(2)
    def click_cancel(self):
        self.driver.find_element('xpath',self.cancel).click()
        time.sleep(2)
    def click_cancel_confirm(self):
        self.driver.find_element('xpath',self.confirm_cancel).click()
        time.sleep(2)


