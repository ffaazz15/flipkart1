class ProductPage():
    def __init__(self, driver):
        self.driver = driver

        self.select_iphone_link_xpath = "/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]"

    def click_iphone(self):
        self.driver.find_element_by_xpath(self.select_iphone_link_xpath).click()