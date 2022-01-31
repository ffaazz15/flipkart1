from selenium.webdriver.common.keys import Keys


class HomePage():
    def __init__(self, driver):
        self.driver = driver

        self.search_textbox_xpath = "/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input"
        self.verify_button_xpath = "/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input"

    def enter_search(self, search):
        self.driver.find_element_by_xpath(self.search_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.search_textbox_xpath).send_keys(search)

    def click_verify(self):
        self.driver.find_element_by_xpath(self.verify_button_xpath).send_keys(Keys.ENTER)


