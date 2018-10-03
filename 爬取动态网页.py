#-*- coding: utf-8 -*-

#爬取动态网页

import requests
import demjson

with open('E:\微信宣传稿\豆瓣电影.csv', 'w', encoding='utf-8') as f:
    for n in range(3):
        url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=%E5%8A%B1%E5%BF%97&start={}'.format(n * 20)
        file = requests.get(url).json()
        for i in range(20):
            dicts = file['data'][i]
            title = dicts['title']
            rate = dicts['rate']
            directors = dicts['directors']
            casts = dicts['casts']
            url = dicts['url']
            f.write('{},{},{},{},{}\n'.format(title,directors,rate,' '.join(casts),url))