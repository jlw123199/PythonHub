# -*- coding: utf-8 -*-

import requests
import re

from requests_html import HTMLSession
from bs4 import BeautifulSoup


session = HTMLSession()

def getHTML(url):
    try:
        spliterLine = "--" * 30
        response = session.get(url)
        soup = BeautifulSoup(response.content,'html.parser')

        typeList = soup.find("ul",id="cate_item")
        print (typeList)
        print(spliterLine)

        typeTitleList = typeList.find_all("a")
        print(typeTitleList)
        print(spliterLine)
        for item in typeTitleList:
            print(item)

        # print(response.content)
        # print(soup)
    except Exception as ex:
        print(ex)


def main():
    url = "https://www.cnblogs.com/"
    getHTML(url)



if __name__ == '__main__':
    main()