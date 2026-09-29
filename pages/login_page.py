import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    email='//input[@placeholder="you@example.com"]'
    password='//input[@placeholder="Enter your password"]'
    submit="//span[text()='Sign In']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def pass_mail(self, mail):
        self.driver.find_element('xpath', self.email).send_keys(mail)

    def pass_pwd(self, passw):
        self.driver.find_element('xpath', self.password).send_keys(passw)

    def submit_button(self):
        submit = self.wait.until(
            EC.element_to_be_clickable(
                ('xpath', self.submit)
            )
        )
        time.sleep(3)
        # self.driver.execute_script(
        #     "arguments[0].scrollIntoView({block: 'center'});",
        #     submit
        # )
        ActionChains(self.driver).scroll_to_element(submit).perform()

        submit.click()


        # submit.click()
        time.sleep(2)