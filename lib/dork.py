#-*- coding: utf-8 -*-
# CODENAME : JaxBCD
# github : https://github.com/jaxBCD
import requests,re,os
from urllib.parse import unquote
from fake_useragent import UserAgent
from .tmp import *
from .sqlerror import sql_errors

class dork:

      links = []


      __url = ['',
            'https://www.bing.com/search?q={}&first={}',
            'https://search.yahoo.com/search?p={}&b={}',
            'https://www.google.com/search?q={}&start={}',
            'http://www.baidu.com/s?wd={}&pn={}',
            'https://yandex.com/search?text={}&lr={}'
              ]

      __regex = ['',
                 '<h2><a href="(.+?)" h=',
                 'class=" ac-algo fz-l ac-21th lh-24" href="(.*?)"',
                 'class="r"><a href="/url\?q=(.*?)&amp',
                 ",'mu':'(.*?)'",
                 'target=_blank href="(.*?)" data-'
                ]

      user_agent = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-A800F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/8.2 Chrome/63.0.3239.111 Mobile Safari/537.36'}

      def __init__(self,query,max_page,proxy=None):
          self.proxy = {
                        'http':proxy,
                        'https':proxy
                        }
          self.query = query
          self.max_page = max_page
          self.headers = {'User-agent':UserAgent().random}


      @property
      def bing(self):
          for bing in range(1,(self.max_page+1)):
              url = dork.__url[1].format(self.query,str(bing))
              resp = requests.get(url,proxies=self.proxy,headers=self.headers)
              link = re.findall(dork.__regex[1],unquote(resp.text))
              for urls in link:
                  dork.links.append(urls)
          return dork.links

      @property
      def yahoo(self):
          for yahoo in range(1,(self.max_page+1)):
              url = dork.__url[2].format(self.query,str((self.max_page-1)*10))
              resp = requests.get(url,proxies=self.proxy)
              link = re.findall(dork.__regex[2],unquote(resp.text))
              for urls in link:
                  dork.links.append(urls)
              return dork.links

      @property
      def google(self):
          for google in range(1,(self.max_page+1)):
              url = dork.__url[3].format(self.query,str(google))
              resp = requests.get(url,proxies=self.proxy)
              link = re.findall(dork.__regex[3],unquote(resp.text))
              for urls in link:
                  dork.links.append(urls)
          return dork.links

      @property
      def baidu(self):
          for baidu in range(1,(self.max_page+1)):
              url = dork.__url[4].format(self.query,str(baidu))
              resp = requests.get(url,headers=dork.user_agent,proxies=self.proxy)
              link = re.findall(dork.__regex[4],unquote(resp.text))
              for urls in link:
                  dork.links.append(urls)
          return dork.links

      @property
      def yandex(self): #Yandex sensitive with captcha
          for yandex in range(1,(self.max_page+1)):
              url = dork.__url[5].format(self.query,str(yandex))
              resp = requests.get(url,headers=dork.user_agent,proxies=self.proxy)
              if '{"captchaSound"' in resp.text:
                 print('[Yandex] Captcha Detect')
                 continue
              else:
                 link = re.findall(dork.__regex[5],unquote(resp.text))
                 for urls in link:
                     dork.links.append(urls)
          return dork.links


class sqlscan:

      def __init__(self,url):
          self.url = url

      @property
      def scan(self):
          path = os.getcwd()
          vuln = 0
          res = requests.get(self.url+"'").content
          for typ,error in sql_errors.items():
              if re.search(error, str(res)):
                 vuln += 1
                 file = open(path+'/vuln.txt', 'a+')
                 file.write(self.url+'\n')
                 file.close()
                 print(B+'[+]'+W+' Error : '+R+error+W)
                 print(Y+'[+]'+W+'Type  : '+typ)
              else:
                 pass

          if vuln > 0:
             print(G+"[*]"+W+" Vulnerability")
             print('Url : '+self.url+'\n')
          else:
             print(R+"[-]"+W+" Not Vulnerability")
             print('Url : '+self.url+'\n')

