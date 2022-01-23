from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
parentHandle = driver.current_window_handle
print(parentHandle)
driver.get("https://www.flipkart.com/")
time.sleep(2)

emailId = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
emailId.send_keys("mohammedfazil196@gmail.com")
time.sleep(2)

password = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input")
password.send_keys("Test1")
time.sleep(2)


#submit button
driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button").click()
time.sleep(1)

searchBar = driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
searchBar.send_keys('iPhone 13')
time.sleep(1)

searchButton = driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
searchButton.click()
time.sleep(2)

requiredIphone = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[1]/div[2]/div[6]/div/div/div/a/div[2]/div[1]/div[1]')
requiredIphone.click()
time.sleep(2)
#new window opens
all_handles = driver.window_handles
print(all_handles)

for handle in all_handles:
    if handle != parentHandle:
        driver.switch_to.window(handle)
        buyNow = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[2]/form/button')
        buyNow.click()
        time.sleep(2)
        break

        #edit adress per click karega
driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div[2]').click()
time.sleep(1)

name = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div[2]/label/div[2]/div/form/div/div[2]/div[1]/input')
name.send_keys("Test automation")
time.sleep(1)

phoneNo = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div[2]/label/div[2]/div/form/div/div[2]/div[2]/input')
phoneNo.send_keys("9999999999999")
time.sleep(1)

pinCode = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div[2]/label/div[2]/div/form/div/div[3]/div[1]/input')
pinCode.send_keys("411013")
time.sleep(1)

locality = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div[2]/label/div[2]/div/form/div/div[3]/div[2]/input')
locality.send_keys("dummy")
time.sleep(1)

Address = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div[2]/label/div[2]/div/form/div/div[4]/div/div[1]/textarea')
Address.send_keys("Neova solutions pvt ltd")
time.sleep(2)

city = driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div[2]/label/div[2]/div/form/div/div[5]/div[1]/div[1]/input')
city.send_keys("pune")
time.sleep(2)

#deliver submit
driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div[1]/div[2]/div/div/div/div[2]/div[2]/label/div[2]/div/form/div/div[8]/button[1]').click()
time.sleep(1)

driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div/div[3]/button[1]').click()
time.sleep(2)

#continue to payment options
driver.find_element_by_xpath('//*[@id="to-payment"]/button').click()
time.sleep(800)



#--------------------------------------------------------------check required
#phonepe button

driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div[1]/div[4]/div/div/div[1]/div/label[1]/div[2]/div/div/div[3]/label[1]/div[1]').click()
time.sleep(3)
#continue
driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/div/div[1]/div[4]/div/div/div[1]/div/label[1]/div[2]/div/div/div[3]/label[1]/div[2]/div/button').click()
time.sleep(800)





