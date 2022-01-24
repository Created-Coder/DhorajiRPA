from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.pakwheels.com/used-cars/search/-/')
# Open Webpage on ChromeDriver

flag = True

while flag:
    try:
        btn = driver.find_element_by_xpath("//a[@rel='next']")
        btn.click()
        time.sleep(5)

    except:
        flag = False
#Send Keys

# input = driver.find_element_by_xpath("//input[@id='home-query']")
# input.send_keys("Suzuki")


time.sleep(5)
# Waits (Implicit Wait)
# driver.implicitly_wait(20)
# price = driver.find_element_by_xpath("//span[@class='_56dab877']")
# print(price.text)

# Wait Explicit
# wait = WebDriverWait(driver, 10)
# price = wait.until(
#         EC.presence_of_element_located((By.XPATH, "//span[@class='_56dab877']"))
#     ).text
#
# print(price)



# time.sleep(2)

# Finding Element by Xpath
# link = driver.find_element_by_xpath("(//div[@class='ee2b0479'])[1]")

#Click()
# link.click()

#get Attribute
# imgSrc = driver.find_element_by_xpath("(//img[@class='_5b8e3f79'])[1]").get_attribute('src')
# print(imgSrc)

# imgSrc.click()

# Find ELements By Xpath
# imgSrc = driver.find_elements_by_xpath("//img[@class='_5b8e3f79']")
# for i in imgSrc:
#     print(i.get_attribute('src'))

# time.sleep(2)
#to go Backward

# driver.back()

# time.sleep(2)
#to go Forward

# driver.forward()

# time.sleep(2)

# Close ChromeDriver
driver.close()