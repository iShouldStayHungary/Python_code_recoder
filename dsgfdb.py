#-*- coding: utf-8 -*-

import requests
from lxml import etree

url = 'https://m.baidu.com/sf/vsearch?pd=image_content&word=%E8%A3%B8%E9%9C%B2%E5%A5%B3&tn=vsearch&atn=page&sa=vs_img_indextop&fr=index'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36'}
data = requests.get(url,headers=headers).text

s = etree.HTML(data)
i = 0
file = s.xpath('//*[@id="super-frame"]/div/b-superframe-body/div[1]/div/div[1]/div/div/div/div[7]/div[1]/div[1]/div[1]')
print(file)
for n in file:
    image_url = n.xpath('./div/a/div/img/text()')
    print(image_url)
    image = requests.get(image_url, headers=headers)
    with open('E:/微信宣传稿/image/' + i + '.jpg', 'wb') as f:
        i = i + 1
        print(i)
        f.write(image.content)

