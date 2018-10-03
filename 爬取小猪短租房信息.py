#-*- coding:utf-8 -*-

import requests
from lxml import etree
#使用循环爬取静态网页的信息，并写入本地文档
with open('E:\微信宣传稿\小猪短租房信息.txt', 'w', encoding='utf-8') as f:
    for n in range(5):
        url = 'http://cd.xiaozhu.com/search-duanzufang-p{}-0/'.format(n)
        data = requests.get(url).text
        s = etree.HTML(data)
        file = s.xpath('//*[@id="page_list"]/ul/li')
        for div in file:
            name = div.xpath('./div[2]/div/a/span/text()')[0]
            scale = div.xpath('./div[2]/div/em/text()')[0].strip()
            score = div.xpath('./div[2]/div/em/span/text()')[0].strip().strip("-")
            price = div.xpath('./div[2]/span[1]/i/text()')[0]
            f.write("名称：{}\n".format(name))
            f.write("规模：{}\n".format(scale))
            f.write("价格：{}\n".format(price))
            f.write("评分：{}\n\n".format(score))

