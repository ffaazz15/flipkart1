class PaymentPage():
    def __init__(self, driver):
        self.driver = driver

        self.select_phonepay_button_xpath = "/html/body/div[1]/div/div[2]/div/div[1]/div[4]/div/div/div[1]/div/label[1]/div[2]/div/div/div[3]/label[1]/div[1]"
        self.select_continue_button_xpath = "//button[@class='_2KpZ6l _3JboYb _3AWRsL']"

    def click_phonepay(self):

        self.driver.find_element_by_xpath(self.select_phonepay_button_xpath).click()

    def click_continue_button(self):

        self.driver.find_element_by_xpath(self.select_continue_button_xpath).click()