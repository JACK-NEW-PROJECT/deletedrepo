#-*- coding: utf-8 -*-
from mechanicalsoup import StatefulBrowser
from re import findall
from .useragent import useragent
from .tmp import load

class scrape(StatefulBrowser):

      def __repr__(
        fitur = {
            'features':'html.parser',
        },
        uag = useragent()
      ):
          return StatefulBrowser(
            soup_config = fitur,
            user_agent = useragent
          )

class Parser(object):

      __list = []

      def __init__(
        self,
        dork,
        URL,
        pattern,
        class_tag,
        proxy = None
      ):
          self.dork = dork
          self.URL = URL
          self.__pattern = pattern
          self.class_tag = class_tag
          self.proxy = {
            'https':proxy
          }
          
          
      def __dir__(self):
          return list(set(self.__list))

          
      def get_page(self):
          self.__req = scrape()
          s = self.__req.open(
            self.URL,
            proxies = self.proxy,
            timeout = 10
          )
          self.__req.select_form(
            'form[action="/search"]'
          )
          self.__req['q'] = self.dork
          self.__req.submit_selected()
          _content = str(self.__req.get_current_page())
          for urls in findall(
            self.__pattern,
            _content                        
          ):  
              if 'www.google.com' in self.URL: self.__list.append(urls)
              else: self.__list.append(urls[:-1])
          return self.__req.get_current_page().find_all(
            'a',
            class_=self.class_tag
          )
          
      def request(self):
          self.__req = scrape()
          for page in self.get_page():
              try:
                  load()
                  self.__req.open(
                    f'{self.URL}{page.get("href")}',
                    proxies = self.proxy
                  )
                  content = str(self.__req.get_current_page())
                  for urls in findall(
                  self.__pattern,
                  content
                  ):
                      if 'www.google.com' in self.URL: self.__list.append(urls)
                      else: self.__list.append(urls[:-1])
              except Exception as e:
                  print(e)  



