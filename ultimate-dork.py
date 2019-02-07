#-*- coding: utf-8 -*-
import sys,os
from lib.tmp import *

if sys.version[0] in '2':
   exit('\n'+R+'[!]'+W+' Please Use Python 3 To Run This Tool'+'\n')

try:
   import requests,argparse,textwrap
except ModuleNotFoundError as e:
   print(e)
   exit(R+'[!]'+W+'type "python3 -m pip install requests" To Install')

from lib.dork import sqlscan
from lib.dork import dork
from requests.exceptions import *
ERROR =[R+'[x]'+W+' Internet Connection Error Or No internet Connection',
        R+'[!]'+W+' Invalid Proxy e.g 127.0.0.1:1337',
        R+'[!]'+W+' Proxy Error Connection']

nani = []
class search(dork):

      def __init__(self,dork,page,proxy=None):
          try:
             super().__init__(dork,
                              page,
                              proxy)
             print(G+'!Info:'+W+' Searching on Google')
             for a in super().google:
                 nani.append(a)
             print(G+'!Info:'+W+' Searching on Bing')
             for b in super().bing:
                 nani.append(b)
             print(G+'!Info:'+W+' Searching on Yahoo')
             for c in super().yahoo:
                 nani.append(c)
             print(G+'!Info:'+W+' Searching on Baidu')
             for d in super().baidu:
                 nani.append(d)
             print(G+'!Info:'+W+' Searching on Yandex')
             for e in super().yandex:
                 nani.append(e)
          except ConnectionError:
             print(ERROR[0])
          except InvalidProxyURL:
             print(ERROR[1])
          except ProxyError:
             print(ERROR[2])
          except KeyboardInterrupt:
             sys.exit('Exit...')

def sqliscan(url):
    try:
         sqlscan(url).scan
    except ConnectionError:
         print(ERROR[0])
    except InvalidSchema:
         pass
    except InvalidURL:
         pass
    except MissingSchema:
         pass
    except ConnectTimeout:
         print(ERROR[0])
    except HTTPError:
         pass
    except TooManyRedirects:
         pass
    except KeyboardInterrupt:
         sys.exit('Exit....')


fel = sys.argv[0]
par = argparse.ArgumentParser(
prog=fel,
usage="%(prog)s --key [keyword] --max-page [number] --scan",
formatter_class=argparse.RawTextHelpFormatter,
description="""
Descriptions:
-----------------------------
Dorking Url Use Search Engine
and Scan SQLi Vulnerability
Search Engine:
+ Google
+ Bing
+ Yahoo
+ Baidu
+ Yandex
""")

par.add_argument(
'--key',
help="""
Your KeyWord e.g Hello
if the word key is more than one, use plus key
e.g Hello+world

""",
metavar='[keywords]',
type=str)
par.add_argument(
'--proxy',
help='''
if using proxy e.g 127.0.0.1:1337
with auth e.g user@pass:127.0.0.1:1337

''',
metavar='[proxy:port]',
type=str,
action='store',
default=None)
par.add_argument(
'--max-page',
type=int,
metavar='[page]',
help="max page crawl url type must be integer or number")
par.add_argument(
'--scan',help="if with Scan SQL injection Vulnerability Use This argument",action="store_true")
arg = par.parse_args()
if arg.scan:
   if arg.key != None and arg.max_page != None:
      print(logo)
      search(arg.key,arg.max_page,proxy=arg.proxy)
      for i in nani:
          print(' - '+i)
      print(G+"!Info :"+W+" Start scan SQLi Vulnerability !")
      for i in nani:
          sqliscan(i)
   else:
      par.print_help()
          
          
elif not arg.scan:
   if arg.key != None:
      print(logo)
      search(arg.key,arg.max_page,proxy=arg.proxy)
      for i in nani:
          print(' - '+i)
   else:
      par.print_help()
else:
   par.print_help()




