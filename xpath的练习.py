#-*- coding:utf-8 -*-

import requests
from lxml import etree
import csv
import time

head = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36"}

with open('E:\微信宣传稿\Q房网房源信息.csv','w',encoding='utf-8') as f:
    for n in range(1, 50):
        url = 'https://qingdao.qfang.com/garden/n{}'.format(n)
        bd = requests.get(url, headers=head).text
        s = etree.HTML(bd)
        file = s.xpath('//*[@id="cycleListings"]/ul/li')
        for div in file:
            name = div.xpath('./div[1]/p[1]/a/text()')[0].strip().strip('\t')
            number = div.xpath('./div[1]/p[2]/b[2]/a/text()')
            constract_time = div.xpath('./div[1]/p[3]/span[3]/text()')
            address = div.xpath('./div[1]/p[4]/span/text()')
            adventage_price = div.xpath('./div[2]/p[1]/span[1]/text()')[0].strip().strip('\t')
            f.write('{},{},{},{},{}元/平米\n'.format(name,address,number,constract_time,adventage_price))