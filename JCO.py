# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 04:04:42 2017

@author: aldos
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pymysql

def getName(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read(), "lxml")
    name = bsObj.find("div",{"class":"row nomargin"}).findAll("h4")
    
    return name

def getAddress(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html.read(), "lxml")
    addresses = bsObj.findAll("div", {"class":"row nomargin storelist"})
    alamats=[]
    kotas=[]
    for address in addresses:
        try:
          a = address.find("div",{"class":"col-md-6"})
        except:
          pass
        try:
          alamat = a.find('h4').next_sibling.replace("\n"," ")
          alamats.append(alamat)
          kota = a.find('br').next_sibling
          kotas.append(kota)
        except:
            pass
    
    return alamats,kotas

#conn = pymysql.connect(host='localhost', port='', user='root', passwd='', db='webcrawling', charset='utf8')
#cur = conn.cursor()

html = urlopen("http://www.jcodonuts.com/id/location")
bsObj = BeautifulSoup(html.read(), "lxml")

kota = bsObj.find("div",{"class":"citylist product-name"}).findAll("a")
j = 0

#cur.execute("TRUNCATE TABLE jco")
#cur.connection.commit()

for k in kota:
  print(kota[j].attrs['href'])
  name = getName(kota[j].attrs['href'])
  address,city = getAddress(kota[j].attrs['href'])
  index = 0
  
  for i in name:
      print(i.get_text())
      #cur.execute("INSERT INTO jco (Name, Address, City) VALUES (%s, %s, %s)", (i.get_text(), address[index], city[index]))
      #cur.connection.commit()
      index = index + 1
  
  j = j + 1
  
#cur.close()
#conn.close()

