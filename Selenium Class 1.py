from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')

# Open Webpage on ChromeDriver
driver.get('https://www.olx.com.pk/mobile-phones_c1453')

time.sleep(5)

# Finding Element by Xpath
link = driver.find_element_by_xpath("(//div[@class='ee2b0479'])[1]")

#Click()
link.click()

time.sleep(2)
#to go Backward

driver.back()

time.sleep(2)
#to go Forward

driver.forward()

time.sleep(2)

# Close ChromeDriver
driver.close()