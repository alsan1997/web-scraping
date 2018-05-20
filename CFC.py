# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 00:38:34 2017

@author: aldos
"""

from bs4 import BeautifulSoup
import requests, json
import pymysql

#def save(result):
     #cur.execute("INSERT INTO cfc (lokasi, source, nama, alamat, telepon, icons, latitude, longitude) VALUES (%s, %s, %s,%s, %s, %s,%s, %s)",
                 #(result['lokasi'], result['source'], result['nama'],result['alamat'],result['telepon'],  result['icons'],result['latitude'], result['longitude']))
        
     #cur.connection.commit()           

      
def extract(soup, kota):
    data = {}
    loc=soup.find('ul',{'class':'location_list'}).find_all('li')

    for i in soup.find_all('script'):
        if 'var points' in i.getText():
            sc = i.getText().split('var points =')[1].split(';')[0]
            jsonObj = json.loads(sc)
            
            for j in jsonObj:
                data[j['id']]=j['lat']+','+j['lng']
            break
        
    for l in loc:
        a=l.find('a')
        try:
          marker=a['onclick'].split('(')[1].replace(');','').strip() 
        except:
          continue
          
        result={}
        result['lokasi']=kota
        result['source']='cfcindonesia.com'
        result['nama']=a.getText().strip()
        
        con='\n'.join([i.getText() for i in l.find_all('div')]).split('Telp.')        
            
        result['alamat']=con[0].strip()
        
        try:
            result['telepon']=con[1].strip()
        except:
            result['telepon'] = ''
        
        try:
            icon=l.find('ul',{'class':'icon_list'}).find_all('li')
            result['icons']=', '.join([i['title'] for i in icon])
        except:
            result['icons'] = ''
        #print("data is", data)
        try:
            latLng=data[marker].split(',')
            result['latitude']=latLng[0]
            result['longitude']=latLng[1]
            #print(latLng)
        except Exception:
            print("error")
        
        #save(result)
        print(result)
        #print(marker)
        
#conn = pymysql.connect(host='localhost', port='', user='root', passwd='', db='webcrawling', charset='utf8')
#cur = conn.cursor()   

#cur.execute("TRUNCATE TABLE cfc")
#cur.connection.commit()

ua="Mozilla/5.0"
url="http://www.cfcindonesia.com/lokasi"

req=requests.get(url,headers={'User-agent':ua}).content
soup=BeautifulSoup(req,'html.parser')

print("----------")
for i in soup.find('select',{'id':'selectProvince'}).find_all('option'):
    print(i)
    value=i['value']
    if(value == ""):
        continue
    #print(value)
    params = {'selectProvince':value,'Submit':'Cari'}
    req = requests.post(url, data = params).content
    soup = BeautifulSoup(req, 'html.parser')
    extract(soup, i.getText().strip())
    