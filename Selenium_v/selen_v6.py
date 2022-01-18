import time
import datetime as date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import pandas as pd

#reference:
#https://www.youtube.com/watch?v=b5jt2bhSeXs
#https://chromedriver.chromium.org/home

count = 0
break_count = 0
while count < 40: #5hrs
  try:
    s=Service('/home/hman/Downloads/chromedriver')  
    cc = pd.read_csv('/home/hman/Documents/dash.coin/cc_data.csv')
    path = '/home/hman/Downloads/chromedriver'  # Optional argument, if not specified will search path.
    site = 'https://unmineable.com/coins/SHIB/address/0x46406393e7364889c3113e0760b4a7a729111fc2'
    driver = webdriver.Chrome(service=s)  # Optional argument, if not specified will search path.
    driver.get(site)
    time.sleep(8)
    pending = driver.find_element(By.ID,"pending_balance")
    active_workers = driver.find_element(By.ID,"active_workers")
    hr = driver.find_element(By.XPATH,'//*[@id="content"]/div/div/div[2]/div[3]/div/div[3]/div[2]/div[2]/table/tbody/tr/td[2]')
    hr1 = hr.get_attribute('innerHTML')
    curr_hr = hr1[:2]
    calc_hr = hr1[hr1.find('(')+1:hr1.find(')')]
    diff = float(pending.text)-pd.to_numeric(cc['Num_Coins'].iloc[-1])

    ls = [date.datetime.now().date(),date.datetime.now().time(),pending.text,curr_hr,calc_hr,diff]
    diff = float(pending.text)-pd.to_numeric(cc['Num_Coins'].iloc[-1])
    len_cc = len(cc)
    cc.loc[len_cc] = ls
    count += 1
    print(ls)
    cc.to_csv('/home/hman/Documents/dash.coin/cc_data.csv',index=False) 
    driver.quit()
    time.sleep(60*15)
  except Exception as e:
    if break_count < 3:
      print(e)
      break_count += 1
      time.sleep(60*5)
      continue 
    else:
      break
