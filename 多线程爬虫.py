#-*- coding:utf-8 -*-

import requests
from lxml import  etree
import csv
from multiprocessing.dummy import Pool as pl #导入线程池


def spider(url):
    datas = requests.get(url, headers=headers).text
    room = etree.HTML(datas)
    name = room.xpath('/html/body/div[2]/div/div[1]/h2/text()')[0]
    address = room.xpath('/html/body/div[2]/div/div[1]/div/text()')[0]
    average_price = room.xpath('//*[@id="headInfo"]/div/div[2]/div[1]/p[2]/span/text()')[0]
    property = room.xpath('//*[@id="headInfo"]/div/div[2]/div[2]/ul/li[5]/p/text()')
    park_number = room.xpath('//*[@id="headInfo"]/div/div[2]/div[2]/ul/li[2]/p/text()')
    image_url = room.xpath('//*[@id="previewCon"]/img/@src')[0]
    image = requests.get(image_url, headers=headers)
    with open('E:/微信宣传稿/图片/Q房网图片信息/' + name + '.jpg', 'wb') as f:
        f.write(image.content)
    with open('E:\微信宣传稿\房源信息.csv', 'w', encoding='utf-8') as f:
        f.write("{},{},{},{},{}\n".format(name, address, average_price, property, park_number))
    print('正在爬取：', name)

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36'}
    pool = pl()
    all_url = []
    for n in range(1, 50):
        start_url = 'https://qingdao.qfang.com/garden/n{}'.format(n)
        data = requests.get(start_url, headers=headers)
        message_tree = etree.HTML(data.text)
        file = message_tree.xpath('//*[@id="cycleListings"]/ul/li')[0]
        i = 0
        for m in file:
            xiaoqu_url_afters = m.xpath('//*[@id="cycleListings"]/ul/li/a/@href')
            i = i + 1
            xiaoqu_url_after = xiaoqu_url_afters[i]
            xiaoqu_url = 'https://qingdao.qfang.com' + xiaoqu_url_after
            #spider(xiaoqu_url)
            all_url.append(xiaoqu_url)
        print(all_url)
        pool.map(spider, all_url)
    pool.close()
    pool.join()