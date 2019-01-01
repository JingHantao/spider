#-*-coding:utf-8-*-
import requests
import os
import time
from bs4 import BeautifulSoup
from io import BytesIO
from PIL import Image

url = 'http://desk.zol.com.cn/bizhi/6338_78073_2.html'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
request = requests.get(url ,headers = header)
soup = BeautifulSoup(request.content,'html.parser')
itmes = soup.find_all('img',id="bigImg")
for index,itme in enumerate(itmes):
    html = requests.get(itme.get('src'))#获取图片地址
    print 'dowloading......'
    image_name = 'picture' + str(index+1) + '.png'
    image = Image.open(BytesIO(html.content))
    image.save('/home/jinghantao/图片/pictures/spider1/' + image_name)
    print 'finishing.......'
