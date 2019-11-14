# -*- coding: utf-8 -*-
import crawler
import requests
from requests_html import HTMLSession

if __name__ == '__main__':

    print("greet!")

    session = HTMLSession()
    url = "http://www.sina.com.cn/"
    r = session.get(url)
    print(r.html.text)

    print ("greet!")
    url = "https://www.cnblogs.com/"
    cnblogsIndexPage = crawler.get_html(url)
    print (cnblogsIndexPage)
