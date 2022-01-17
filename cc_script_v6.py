import requests
import datetime as date
import pandas as pd
import time
import sys

wall = '0x46406393e7364889c3113e0760b4a7a729111fc2'
c = 'SHIB'
u = '036b48cf-69d3-483c-90e0-cbd75b62d6b6'

address = 'https://api.unminable.com/v4/address/'+wall+'?coin='+c
worker = 'https://api.unminable.com/v4/account/'+u+'/workers'
u_workers = 'https://api.unminable.com/v4/account/'+u+'/workers'

cc = pd.read_csv('cc_data.csv')

addy = requests.get(address)
addy_bal = addy.json()['data']['balance']

ls = [date.datetime.now().date(),date.datetime.now().time(),addy_bal]
hash = ['rhr','chr']
count = 0
break_count = 0

while count < 20:
  try: 
    ls = [date.datetime.now().date(),date.datetime.now().time()]
    addy = requests.get(address)
    ls.append(addy.json()['data']['balance'])
    for h in hash:
      hr = requests.get(u_workers)
      ls.append(hr.json()['data']['ethash']['workers'][0][h])
  
    #diff=float(ls[2])-cc['Num_Coins'].iloc[-1] 
    #print(float(ls[2]))
    #print(type(cc['Num_Coins'].iloc[-1]))
    #print(float(ls[2])-cc['Num_Coins'].iloc[-1])
    diff=float(ls[2])-pd.to_numeric(cc['Num_Coins'].iloc[-1])
    ls.append(diff) 
    count+=1
    len_cc = len(cc)
    cc.loc[len_cc] = ls
    cc.to_csv('cc_data.csv', index=False)
    print(ls)
    #print('try')
    time.sleep(60*15) #15min
  except Exception as e:
    if break_count < 3:
      ls = [date.datetime.now().date(),date.datetime.now().time()]
      addy = requests.get(address)
      ls.append(addy.json()['data']['balance'])
      #for h in hash:   #manually add chr and chr no loop
      #  hr = requests.get(u_workers)
      #  ls.append(0)
      #ls.append(requests.get(u_workers).json()['data']['ethash']['workers'][0]['rhr'])
      #ls.append(0)
      #print(requests.get(u_workers).jason()['data']['ethash'])
      print(e)

      
      #diff=float(ls[2])-cc['Num_Coins'].iloc[-1] 
      #ls.append(diff) 
      #count+=1
      #break_count+=1
      #len_cc = len(cc)
      #cc.loc[len_cc] = ls
      #cc.to_csv('cc_data.csv', index=False)
      #print(ls)
      #time.sleep(60*2) #15min
     
      #diff = ls[2]-cc['Num_Coins'][-1:]
      #ls.append(diff) 
      #print(ls)
      #count +=1
      #break_count+=1
      #len_cc = len(cc)
      #cc.loc[len_cc] = ls
      #cc.to_csv('cc_data.csv',index=False)
      #print('except')
      time.sleep(60*2) #15min
    else:
      print(sys.stderr, 'does not exist')
      #print(sys.stderr, 'Exception: %s', % str(e)
      sys.exit(1) 
