#-*-coding:utf-8-*-
import urllib2
import urllib
import ssl
import re
import lxml
from bs4 import BeautifulSoup

# def get_content(html):
#     list=[]
#     div_con=re.compile(r'<div.*? class="ie-fix">(.*?)</div>',re.S|re.M)
#     item_list=re.findall(div_con,html)
#     for item in item_list:
#         list.append(item )
#     return list

def get_content(html):
    list = []
    res_div = r'<div.*? class="ie-fix">(.*?)</div>'
    item_list = re.findall(res_div, html, re.S | re.M)
    for item in item_list:
        # item = item.replace("<span>", "").replace("</span>","").replace("\n","").replace("</br>","").replace("<br/>","")
        list.append(item)
        # list.append("\n")
    return list

req = urllib2.Request('http://desk.zol.com.cn/bizhi/6338_78073_2.html')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
html = urllib2.urlopen(req).read()
soup = BeautifulSoup(html, 'lxml')
print soup
#print get_content(soup)
#print html
