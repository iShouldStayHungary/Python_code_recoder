#-*- coding:utf-8 -*-

import requests
from lxml import etree

headers = {
'User-Agent': ' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
url = 'https://accounts.douban.com/login'
formdata = {'source': 'index_nav',
'redir': 'https://www.douban.com/',
'form_email': '17866628771',
'form_password': 'shlx1988@'}
s = requests.session()
r = s.post(url, data=formdata)
file = etree.HTML(r.text)
print(file)
da = file.xpath('//*[@id="statuses"]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/div/a/@href')
print(da)
# for n in range(1, 10):
#     dairy = file.xpath('//*[@id="statuses"]/div[2]/div[{}]/div/div/div[2]/div[1]/div[2]/p/text()'.format(n))
#     print(dairy)
#     with open('E:\微信宣传稿\日记.txt', 'w',encoding='utf-8') as f:
#         f.write(dairy)