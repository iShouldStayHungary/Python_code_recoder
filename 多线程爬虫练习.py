#-*- coding: utf-8 -*-

import requests
from lxml import etree
from multiprocessing.dummy import Pool as pl #导入线程池


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36'}
    with open('E:\微信宣传稿\Q房网信息.csv', 'w', encoding='utf-8') as f:
        for n in range(1, 5):
            url = 'https://qingdao.qfang.com/garden/n{}'.format(n)
            data = requests.get(url, headers=headers).text
            data_tree = etree.HTML(data)
            file = data_tree.xpath('//*[@id="cycleListings"]/ul/li')
            print('sasfsgf')
            for room in file:
                name = room.xpath('./div[1]/p[1]/a/text()')[0]
                address = room.xpath('./div[1]/p[4]/span/text()')[0]
                average_price = room.xpath('./div[2]/p[1]/span[1]/text()')[0]
                f.write("{} ,{} , {}\n".format(name, address, average_price))
                print("正在爬取:", name)
