# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
# Excel
from openpyxl import Workbook

def get_html(url):
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
    html = requests.get(url, headers=header).content
    return html



