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
while count < 20:
  cc = pd.read_csv('coin_count1.csv')
  path = '/home/hman/Downloads/chromedriver'  # Optional argument, if not specified will search path.
  site = 'https://unmineable.com/coins/SHIB/address/0x46406393e7364889c3113e0760b4a7a729111fc2'
  driver = webdriver.Chrome(path)  # Optional argument, if not specified will search path.
  driver.get(site)
  time.sleep(6)
  pending = driver.find_element(By.ID,"pending_balance")
  #pending = pending.text
  active_workers = driver.find_element(By.ID,"active_workers")
  #active_workers.text
  date_time = date.datetime.now()
  print(str(date_time)+': '+pending.text+', workers: '+active_workers.text)

  

  ls = [date_time.strftime("%x"),date_time,pending.text,active_workers.text]
  #row = pd.Series(ls,index=cc.columns)
  len_cc = len(cc)
  cc.loc[len_cc] = ls
  count += 1
  cc.to_csv('coin_count1.csv',index=False) 
  driver.quit()
  time.sleep(60*15)
