#-*- coding:utf-8 -*-

import requests
from lxml import etree

def spider(urlp):
    data = requests.get(urlp, proxies=proxies, headers=headers)
    print("spider")
    return etree.HTML(data.text)

def get_all_url(contexts, search_page):
    for n in range(1, int(search_page)+1):
        url1 = 'http://weixin.sogou.com/weixin?query=' + contexts + '&type=2&page=' + str(n) + '&ie=utf8'
        s = spider(url1)
        print("all_url")
        context_url = s.xpath('//*[@id="sogou_vr_11002601_title_"]/@href')
        all_url.extend(context_url)

def detail_context(urls):
    s = spider(urls)
    print("detail")
    title = s.xpath('//*[@id="activity-name"]/text()')[0]
    print(title)
    detail = s.xpath('//*[@id="js_content"]/p[4]/span/text()')[0].strip('')
    print(detail)




if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36'}
    proxies = {
        "http": "http://118.190.95.35",
        "http": "http://118.190.95.43",
        "http": "http://61.135.217.7",
    }
    all_url = []
    context = input("请输入爬取内容：")
    search_pages = input("请输入搜索页数：")
    get_all_url(context, search_pages)
    print(all_url)
    for url in all_url:
        detail_context(url)