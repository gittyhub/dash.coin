import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

path = '/home/hman/Downloads/chromedriver'
site = 'www.google.com'
driver = webdriver.Chrome(path)
driver.get(site)
time.sleep(5)
searchbox = driver.find_element_by_name('q')
searchbox.send_keys('ChromeDriver')
searchbox.submit()
time.sleep(5)
driver.quit()
