#-*- coding: utf-8 -*-
from urllib import request,parse
import json
'''
with request.urlopen('https://www.douban.com/') as f:
    data = f.read()
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s'% (k,v))
    js = data.decode('utf-8')
    f = json.dumps(js)
    print("AAAAAAAAAAAAA")
    result = json.loads(f)
    print(result)
    #print('data:',data.decode('utf-8'))


#模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头
req = request.Request('https://www.douban.com/')
#User-Agent头就是用来标识浏览器的。
req.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    date = f.read()
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s' % (k,v))
    print("date:",date.decode('utf-8'))


print("Login to weixin.cn")
name = input('username:')
password = input('password:')
#向网页发送一个post请求，把登录的参数date用parse.urlencode()转化成byte
Login_date = parse.urlencode([ #把
    ('username',name),
    ('password',password),
    ('entry','mweibo'),
    ('client_id',''),
    ('savestate','1'),
    ('ec',''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
  ])
req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin','https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer','https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req,data = Login_date.encode('utf-8')) as f:
    print("Status:",f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s'% (k,v))
    print('date:',f.read().decode('utf-8'))
'''

#XML操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，
# 因此占用内存大，解析慢，优点是可以任意遍历树的节点。SAX是流模式，
# 边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

from  xml.parsers.expat import ParserCreate
import datetime
from urllib import request
#解析xml
#当SAX解析器读到一个节点时 <a href="/">python</a>会产生3个事件：
#           1:  start_element事件，在读取<a href="/">时；
#           2:  char_data事件，在读取python时；
#           3:   end_element事件，在读取</a>时
class DefaultSaxHandLer(object):
    def start_element(self,name,attrs):
        print('sax:start_element:%s,attrs:%s' % (name,attrs))

    def end_element(self,name):
        print('sax:end_element:%s' % name)

    def char_data(self,text):
        print('sax: char_data:%s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler = DefaultSaxHandLer()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)

class YWeather(object):
    def start_element(self,name,attrs):
        if name == 'results':
            self.result = {}

        if name == 'yweather:location':
             self.result['city'] = attrs['city']

        if name == 'yweather:condition':
            self.result['forecast'] = []

        if name == 'yweather:forecast':
            dt = {
                'date':attrs['date'],
                'high':int(attrs['high']),
                'low': int(attrs['low']),
                'text': attrs['text']
            }
            self.result['forecast'].append(dt)

    def end_element(self,name):
        if name == 'results':
            print(self.result)


    def char_element(self,text):
        pass

def parseXml(xml_str):
    handler = YWeather()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_element
    parser.Parse(xml_str)
    return handler.result

url = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
with request.urlopen(url) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'