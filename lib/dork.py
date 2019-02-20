#-*- coding: utf-8 -*-
import requests,re
from urllib.parse import unquote
from fake_useragent import UserAgent
from .tmp import anim
from .tmp import color as c

class search_engine(object):

      __uag = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-A800F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/8.2 Chrome/63.0.3239.111Mobile Safari/537.36'}
      _url = []

      def __init__(
                   self,
                   keyword,
                   page,
                   proxy=None        
          ):
          self.keyword = keyword
          self.page = page
          self.ua = {'User-Agent':UserAgent().random}
          self.proxy = {
                        'http':proxy,
                        'https':proxy
          }

      @property
      def google(self):
          for google in range(1,(self.page+1)):
              anim(f'{c.G}www.google.com{c.W}')
              resp = requests.get(
                     f'https://www.google.com/search?q={self.keyword}&start={self.page}',
                     proxies=self.proxy
              )
              _link = re.findall(
                      'class="r"><a href="/url\?q=(.*?)&amp',
                      unquote(resp.text)                
              )
              for x in _link:
                  search_engine._url.append(x)
          return search_engine._url

      @property  
      def yahoo(self):
          for yahoo in range(1,(self.page+1)):
              anim(f'{c.G}search.yahoo.com{c.W}')
              resp = requests.get(
                     f'https://search.yahoo.com/search?p={self.keyword}&b={self.page}',
                     proxies=self.proxy
              )
              _link = re.findall(
                      'class=" ac-algo fz-l ac-21th lh-24" href="(.*?)"',
                       unquote(resp.text)
              )
              for x in _link:
                  search_engine._url.append(x)
          return search_engine._url

      @property
      def bing(self):
          for bing in range(1,(self.page+1)):
              anim(f'{c.G}www.bing.com{c.W}')
              resp = requests.get(
                     f'https://www.bing.com/search?q={self.keyword}&first={self.page}',
                     proxies=self.proxy                
              )
              _link = re.findall(
                      '<h2><a href="(.+?)" h=',
                      unquote(resp.text)                
              )
              for x in _link:
                  search_engine._url.append(x)
          return search_engine._url

      @property
      def baidu(self):
          for baidu in range(1,(self.page+1)):
              anim(f'{c.G}www.baidu.com{c.W}')
              resp = requests.get(
                     f'http://www.baidu.com/s?wd={self.keyword}&pn={self.page}',
                     proxies=self.proxy,
                     headers=search_engine.__uag
              )
              _link = re.findall(
                      ",'mu':'(.*?)'",
                      unquote(resp.text)
              )
              for x in _link:
                  search_engine._url.append(x)
          return search_engine._url
 
