#-*-coding:utf-8-*-
import os
import time
import urllib.request
from bs4 import BeautifulSoup
from io import BytesIO

url="https://wenku.baidu.com/view/9c91c0a9dd3383c4bb4cd2ff.html?from=search"
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
request = urllib.request.Request(url = url,headers = header)
response = urllib.request.urlopen(request)
html = response.read()
#print(html)
soup = BeautifulSoup(html,'lxml')
itmes = soup
print(itmes)