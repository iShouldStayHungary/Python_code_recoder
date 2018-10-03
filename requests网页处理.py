#-*- coding:utf-8 -*-
import requests
r = requests.get('https://www.douban.com/')
print(r.status_code)
#传入一个dic作为parmas参数,https的请求头依然可以
t = requests.get('https://www.douban.com/',params = {'q':'python','fish':'000'},headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(t.url)
#实际请求的url:https://www.douban.com/?q=python&fish=000
print(t.encoding )#使用encoding属性查看requests的编码方式
#使用content属性获取bytes对象
print(t.content)
#requests对于特定类型的响应如json，可以直接获取
t = requests.get('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
print(t.json())

h = t.headers
print(h)
for k,v in h.items():
    print(k, ' : ',v)