#-*- coding: utf-8 -*-

import requests

# r = requests.get('https://www.douban.com')
# r.encoding = 'utf-8'
dict = {'user': '2996654722@qq.com', 'password': 'shlx1988@'}
#r = requests.post('https://www.douban.com', data=dict)

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36'}
r = requests.post('https://www.douban.com', data=dict, headers=header, timeout=3)
s = requests.session()#保持登录的状态
#由于反爬虫限制，网站对于一个特定的ip地址设有访问次数的限制，所以设置代理ip很重要
proxies = {
    'http': 'http//10.1.10.12:81',
    'https': 'https//10.1.10.12:81'
}
print(r.status_code)