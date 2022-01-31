from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest
from SampleProject.POMProjectDemo.Pages.loginPage import LoginPage
from SampleProject.POMProjectDemo.Pages.homePage import HomePage
from SampleProject.POMProjectDemo.Pages.newAdress import NewAddrPage
from SampleProject.POMProjectDemo.Pages.paymentPage import PaymentPage
from SampleProject.POMProjectDemo.Pages.productPage import ProductPage
from SampleProject.POMProjectDemo.Pages.buyNow import BuyNowPage
class LoginTest(unittest.TestCase):



    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
       driver = self.driver
       driver.get("https://www.flipkart.com/")

       login = LoginPage(driver)
       login.enter_username("mohammedfazil196@gmail.com")
       login.enter_password("Test1")
       login.click_login()
       time.sleep(4)
       homepage = HomePage(driver)
       homepage.enter_search("iphone13")

       homepage.click_verify()
       time.sleep(4)
       productpage = ProductPage(driver)
       productpage.click_iphone()
       time.sleep(4)

       parentHandle = driver.current_window_handle

       all_handles = driver.window_handles
       print(all_handles)

       for handle in all_handles:
           if handle != parentHandle:
               driver.switch_to.window(handle)
               buynow = BuyNowPage(driver)
               buynow.click_iphone()
               time.sleep(4)
               break

       newaddr = NewAddrPage(driver)
       # newaddr.click_change()
       newaddr.click_edit()
       newaddr.enter_name("Test Automation")
       time.sleep(2)
       newaddr.enter_number("99999999999")
       time.sleep(2)
       newaddr.enter_pincode("411013")
       time.sleep(2)
       newaddr.enter_locality("Dummy")
       time.sleep(2)
       newaddr.enter_address("Neova Solutions Pvt Ltd")
       time.sleep(2)
       newaddr.click_address_type()
       time.sleep(2)
       newaddr.click_save_and_deliver()
       time.sleep(3)
       newaddr.click_continue()

       time.sleep(4)

       pay = PaymentPage(driver)
       pay.click_phonepay()
       time.sleep(2)
       pay.click_continue_button()

       time.sleep(9)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__=='__main__':
    unittest.main




