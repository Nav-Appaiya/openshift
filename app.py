#!/usr/bin/env python
import os, csv, json, requests
from bs4 import BeautifulSoup

url = "https://www.ede.nl/gemeentearchief/collecties/opendata/datasets-gemeentearchief-ede/wederopbouw-gemeente-ede-1940-1945/"
response = requests.get(url)
# parse html
page = BeautifulSoup(response.content, "lxml")


def getURL(page):
    """

    :param page: html of web page (here: Python home page) 
    :return: urls in that page 
    """
    allHrefLinks = page.findAll("a href")
    
    return allHrefLinks

while True:
    url = getURL(page)
    
    if url:
        print(url)
    else:
        break