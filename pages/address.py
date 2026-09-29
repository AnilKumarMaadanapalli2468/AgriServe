class ADDRESS:
    address='//input[@placeholder="Village, District, State"]'
    pin='//input[@placeholder="6-digit pincode"]'
    setup="//button[text()='Complete Setup']"
    def __init__(self,driver):
        self.driver=driver
    def pass_address(self,add):
        self.driver.find_element('xpath',self.address).send_keys(add)

    def pass_pin(self, pincode):
        self.driver.find_element('xpath', self.pin).send_keys(pincode)

    def click_setup(self):
        self.driver.find_element('xpath', self.setup).click()

