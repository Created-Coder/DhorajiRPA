from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.youtube.com/results?search_query=enumerate+python')

# Get Current URL
print(driver.current_url)

# Scroll till the fixed height
# driver.execute_script("window.scrollTo(0, 2000)")

# Scroll till the end of the page
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Image Downloading
# opener = urllib.request.URLopener()
# opener.addheader('User-Agent', 'whatever')
# filename, headers = opener.retrieve(imgSrc, name + ".jpg")

# urlretrieve(imgSrc, name + ".jpg")