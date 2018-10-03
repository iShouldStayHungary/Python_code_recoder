# -*-coding:utf-8 -*-
import requests
import time
from lxml import etree

# url = 'https://movie.douban.com/subject/25882296'
# data = requests.get(url).text
# s = etree.HTML(data)
# film = s.xpath('//*[@id="content"]/h1/span[1]/text()')
# director = s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')
# actors = s.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')
#
# film_type = s.xpath('//*[@id="info"]/span[i]/text()')
# film_length = s.xpath('//*[@id="info"]/span[14]/text()')
# film_time = s.xpath('//*[@id="info"]/span[12]/text()')
# print('电影名称：', film)
# print('导演：',director)
# print('主演：',actors)
# print('电影类型：',film_type)
# print('电影时长：',film_length)
# print('上映时间：', film_time)

# tuple1 = (1,2,3,4)
# tuple2 = ('asdas','dasdas')
# t = tuple1 + tuple2
# print('tuple1:',tuple1[1:3])
# print(t)

#豆瓣图书top250爬取
with open('E:\微信宣传稿\豆瓣图书top250爬取.txt','w',encoding='utf-8') as f:
    for n in range(10):
        url = 'https://book.douban.com/top250?start={}'.format(n * 25)
        data = requests.get(url).text

        s = etree.HTML(data)
        file = s.xpath('//*[@id="content"]/div/div[1]/div/table')
        for div in file:
            title = div.xpath('./tr/td[2]/div[1]/a/@title')[0]
            score = div.xpath('./tr/td[2]/div[2]/span[2]/text()')[0]
            comment = div.xpath('./tr/td[2]/p[2]/span/text()')
            author = div.xpath('./tr/td[2]/p[1]/text()')[0]
            # print("书名：", title)
            # print("作者：", author)
            # print("评分：", score)
            # print("评论：", comment)
            f.write("书名：{}\n".format(title))
            f.write("作者：{}\n".format(author))
            f.write("评分：{}\n".format(score))
            f.write("评论：{}\n".format(comment))
            f.write('\n')
