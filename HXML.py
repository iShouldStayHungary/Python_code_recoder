#-*- coding: utf-8 -*-
from html.parser import HTMLParser
from urllib import request
from html.entities import name2codepoint
'''
class MyHTMLParser(HTMLParser):
    def handle_starttag(self,tag,attrs):
        print('<%s>'% tag)

    def handle_endtag(self, tag):
        print('</%s>'% tag)

    def handle_startendtag(self, tag, attrs):
        print('<s/>'% tag)

    def handle_data(self,data):
        print(data)

    def handle_comment(self, data):
        print('<!--',data,'-->')

    def handle_entityref(self,name):
        print('&%s' % name)

    def handle_charref(self,name):
        print('&#%s' % name)

parser = MyHTMLParser()
parser.feed()
'''
#--------*********有BUG啊，没解决***********——————————————
class ViewMyHtml(HTMLParser):
    def __init__(self):
        self.result = {}

    def handler_starttag(self,tag,attrs):
        if ('class','event-title') in attrs:
            self.result['event-title'] = []

        if  tag == 'time':
            self.result['time'] = []

        if ('class','event-location') in attrs:
            self.result['event-location'] = []

    def handler_endtag(self,tag,data):
        if tag == '/time':
            self.result['time'] = data

        if tag == '/span':
            self.result['event-location'] = data

        if tag == '/h3':
            self.result['event-title'] = data

        if tag == '/li':
           print(self.result)

    def handler_startendtag(self,tag,attrs):
        pass

    def handler_data(self):
        pass

    def handler_comment(self):
        pass

    def handler_entityref(self,name):
        pass

    def handler_charref(self,name):
        pass


url = 'https://www.python.org/events/python-events/'
with request.urlopen(url,timeout=15) as f:
    data = f.read()
parser = ViewMyHtml()
#print(data.decode('utf-8'))
parser.feed(data.decode('utf-8'))

