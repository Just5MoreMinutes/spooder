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


########
# MAIN
########
def rs(_type:str,txt:str) -> str: r.styles(_type,txt)   # type: ignore #: new print lol

class web_spider:

    def __init__(self, __url, __params) -> None:
        self.__url = __url
        self.__params = __params

    @classmethod
    def downloader(get, params:list, output:str) -> str:  # type: ignore
        
        #: find all files
        r = requests.get(get.__url, allow_redirects=True)

        soup = BeautifulSoup(r.content, 'lxml')

        for link in soup.find_all('a'):
            _r = requests.get(link, allow_redirects=True)
            
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