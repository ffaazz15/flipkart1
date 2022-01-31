class BuyNowPage():
    def __init__(self, driver):
        self.driver = driver

        self.select_buy_button_xpath = "/html/body/div[1]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[2]/form/button"

    def click_iphone(self):

        self.driver.find_element_by_xpath(self.select_buy_button_xpath).click()