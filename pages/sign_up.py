import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SIGNUP:
    start_btn="//a[text()='Get Started']"
    name='//input[@placeholder="John Doe"]'
    mail='//input[@placeholder="you@example.com"]'
    password='//input[@placeholder="Create a secure password"]'
    create_account="//span[text()='Create Account']"
    number='//input[@placeholder="9876543210"]'
    conti="//span[text()='Continue']"
    farmer_rent="//p[text()='Browse and book agricultural equipment for your farm']"
    c_btn="//button[text()='Continue']"
    co_btn="//button[text()='Continue']"
    address_ele='//input[@placeholder="Village, District, State"]'
    pin='//input[@placeholder="6-digit pincode"]'
    complete="//button[text()='Complete Setup']"




    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    def click_get_started(self):
        self.driver.find_element('xpath',self.start_btn).click()
        time.sleep(2)
    def click_signup(self):
        sign_up=self.wait.until(EC.element_to_be_clickable(('xpath',self.signup)))
        ActionChains(self.driver).scroll_to_element(sign_up).perform()
        sign_up.click()
        time.sleep(2)
    def pass_name(self,user_name):
        self.driver.find_element('xpath',self.name).send_keys(user_name)
        time.sleep(2)
    def pass_mail(self,email):
        self.driver.find_element('xpath',self.mail).send_keys(email)
        time.sleep(2)
    def pass_pass(self,pwd):
        self.driver.find_element('xpath',self.password).send_keys(pwd)
        time.sleep(2)
    def click_create_account(self):
        account_create=self.wait.until(EC.element_to_be_clickable(('xpath',self.create_account)))
        ActionChains(self.driver).scroll_to_element(account_create).perform()

        account_create.click()
        time.sleep(2)
    def pass_number(self,num):
        self.driver.find_element('xpath',self.number).send_keys(num)
        time.sleep(2)
    def click_continue(self):
        self.driver.find_element('xpath',self.conti).click()
        time.sleep(3)
    def click_farmer(self):
        self.driver.find_element('xpath',self.farmer_rent).click()
        time.sleep(2)
    def click_continue_1(self):
        self.driver.find_element('xpath',self.c_btn).click()
        time.sleep(2)

    def click_continue_2(self):
        self.driver.find_element('xpath',self.co_btn).click()
        time.sleep(3)

    def pass_address(self,address):
        self.driver.find_element('xpath', self.address_ele).send_keys(address)
        time.sleep(3)

    def pass_pin(self,pincode):
        self.driver.find_element('xpath', self.pin).send_keys(pincode)
        time.sleep(3)

    def click_complete(self):
        self.driver.find_element('xpath', self.complete).click()
        time.sleep(3)




