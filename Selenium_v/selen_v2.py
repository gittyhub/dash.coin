import time
import datetime as date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

#reference:
#https://www.youtube.com/watch?v=b5jt2bhSeXs
#https://chromedriver.chromium.org/home

count = 0
while count < 10:
  cc = pd.read_csv('coin_count.csv')
  path = '/home/hman/Downloads/chromedriver'  # Optional argument, if not specified will search path.
  site = 'https://unmineable.com/coins/SHIB/address/0x46406393e7364889c3113e0760b4a7a729111fc2'
  driver = webdriver.Chrome(path)  # Optional argument, if not specified will search path.
  driver.get(site)
  time.sleep(6)
  try:
      pending = WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.ID, "pending_balance"))
      )
      print(str(date.datetime.now())+': '+pending.text)
      c = pending.text
  finally:
      driver.quit()
  count += 1

  ls = [date.datetime.now(),c]
  #row = pd.Series(ls,index=cc.columns)
  len_cc = len(cc)
  cc.loc[len_cc] = ls
  count += 1
  cc.to_csv('coin_count.csv',index=False) 
  time.sleep(60*30)
