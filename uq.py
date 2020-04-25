# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 11:36:16 2020

@author: kylel
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
chrome = webdriver.Chrome()
chrome.get("https://ecshweb.pchome.com.tw/search/v3.3/?q=iphone")
time.sleep(3)

for i in range(5):
    chrome.execute_scripe('window.scrollTo(0,document.body.scrollHeight);')
    time.sleep(1)
    
soup = BeautifulSoup(chrome.page_source,"html.parser")

for each_prod in soup.find_all('h5',class_="prod_name"):
    productName = each_prod.text
    print(productName)
chrome.close()