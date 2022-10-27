########
# IMPORTS
########
#: the standard bs 
import os
import sys

#: web scraping/parsing
import lxml
import requests
import urllib3
from bs4 import BeautifulSoup

#: utilities
import datetime
import json
import zipfile
from typing import Any

#: my modules
from src.handlers.render import render as r
from src.handlers.errors import *


########
# MAIN
########
def rs(_type:str,txt:str) -> str: r.styles(_type,txt)  #: new print lol
def no_none(_list) -> list:
    for _ in range(int(len(_list))): 
        for i in _list: 
            if i != 'None': _list.remove(i) 
            else: continue
def qappend(_list:list, var, items:list) -> list:
    for i in items:
        var.get(items[i])
        _list.append(i)
    no_none(_list)

class web_spider:

    ALL_LINKS = []

    def __init__(self, __url, __params) -> None:
        self.__url = __url
        self.__params = __params

    @classmethod
    def downloader(GET, params:list, output:str) -> str | str('mb') | SPOODER_DLERROR:    # -> tries to download and/or read website content
        
        #: find all files
        r = requests.get(GET.__url, allow_redirects=True)
        GET.ALL_LINKS.append(GET.__url)

        soup = BeautifulSoup(r.content, 'lxml')

        for link in soup.find_all(True):
            GET.ALL_LINKS.append(str(link.get('href')))
            GET.ALL_LINKS.append(str(link.get('src')))
            no_none(GET.ALL_LINKS)

            _r = requests.get([i for i in GET.ALL_LINKS], allow_redirects=True)
            
            pname = link.split('/')[-1][::-1]   # -> get the name of the current page
            if '.' in pname:
                fname = pname.split('.')[-1][::-1]    # -> get the file extension

            else:

                pass



    @classmethod
    def start(update, params:list) -> str:  # type: ignore
        """
        USAGE:

            `spider.start([<url>, <start param>, <start param>, ...])`

        This tells the spider what url to open.
        `spider.start` should always be executed first.
        """
        #: starts spider
        fallback = {}
        rs('info','Starting web spider...')

        #: check url
        tmp = requests.get(params[0])
        fallback['url'] = params[0]
        #: checks if website can be reached
        if tmp.status_code == requests.codes.ok:
            fallback['reached','time'] = True, datetime.datetime()  #: append some shit
            rs('info','Website can be reached!')
            pass
        else:
            fallback['reached','time'] = False, datetime.datetime() #: append some slightly different shit
            rs('error','Website couldn\'t be reached! (' + tmp.status_code + ')')
            sys.exit(1)     # -> exits with error (of any type, not specified. sys.exit(2) could be used in case of a syntax error. possible: 0-127)
        
        update.__url = params[0]
        update.__params = params[1:]
        del params
        del tmp

        #: dump everything for later use
        with open('tmp.json','a') as jf:
            json.dump(fallback)






#---------------------------------------------------------------------------------------------------------------------------------|
#: NOTE NOTE NOTE NOTE NOTE continue at: trying to download website. look at requests, urllib & bs4. those seem to lead somewhere |
#---------------------------------------------------------------------------------------------------------------------------------|
# Also try to use stackoverflow as rarely as possible, use the docs, you can do better than copy-pasting