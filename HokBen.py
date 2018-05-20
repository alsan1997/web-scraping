# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 13:01:32 2017

@author: aldos
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pymysql

conn = pymysql.connect(host='localhost', port='', user='root', passwd='', db='webcrawling', charset='utf8')
cur = conn.cursor()

html = urlopen("http://www.hokben.co.id/location")
bsObj = BeautifulSoup(html.read(), "lxml")

name = bsObj.find("div", {"id":"view_locations"}).findAll("h3")
jam = bsObj.find("div", {"id":"view_locations"}).findAll("p")
address = bsObj.find("div", {"id":"view_locations"}).findAll("div", {"style":"height: 45px"})
x = 1

for i in name:
    cur.execute("INSERT INTO HokBen (Name) VALUES (%s)", (i.get_text()))
    cur.connection.commit()
     
for i in jam:
    cur.execute("UPDATE HokBen SET Hours = (%s) WHERE ID = (%s)", (i.get_text(), x))
    cur.connection.commit()
    x=x+1
    
x = 1
for i in address:
    cur.execute("UPDATE HokBen SET Address = (%s) WHERE ID = (%s)", (i.get_text(), x))
    cur.connection.commit()
    x=x+1
    
#cur.execute("TRUNCATE TABLE HokBen")
#cur.connection.commit()