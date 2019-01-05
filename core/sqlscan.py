#-*- coding: utf-8 -*-
import requests, re, sys, os
from tmp.temp import color, INF
from core import sqlerror


class scan:

      def __init__(self,url):
          self.url = url


      def sqli_scan(self):
          AE = os.getcwd()
          try:
              req = requests.get(self.url+"'").content
              for value, syntax in sqlerror.sql_errors.items():
                  if re.search(syntax, str(req)):
                     f = open(AE+'/vuln.txt', 'a+')
                     print(color.blue+'[+] '+color.white+self.url)
                     f.write(self.url + '\n')
                     f.close()
                     print(color.green+"[!] VULNERABILITY"+color.white)
                     print(color.yellow+"[*] TYPE : "+color.white+value)
                     print("[!] ERROR : "+color.red+syntax+color.white)
                     print("\n")
                  else:
                     pass
          except(requests.exceptions.ConnectionError):
             pass
          except(requests.exceptions.ReadTimeout):
             pass
          except(requests.exceptions.TooManyRedirects):
             pass
          except(requests.exceptions.MissingSchema):
             pass
          except(requests.exceptions.ContentDecodingError):
             pass
          except(requests.exceptions.InvalidURL):
             pass
          except(requests.exceptions.ChunkedEncodingError):
             pass
          except(KeyboardInterrupt):
             sys.exit()


