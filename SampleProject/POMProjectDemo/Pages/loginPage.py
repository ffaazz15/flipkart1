class LoginPage():
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_xpath = "//input[@class='_2IX_2- VJZDxU']"
        self.password_textbox_xpath = "//input[@class='_2IX_2- _3mctLh VJZDxU']"
        self.login_button_xpath = "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button"

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.username_textbox_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.password_textbox_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
