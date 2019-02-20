#-*- coding: utf-8 -*-
import sys,os,argparse,datetime

if sys.version[0] in '2':
   print('This Tool Only Support For python3.x')
   sys.exit()
   
try:
   import requests
except Exception as e:
   print(e)
   print('[!] type, python3 -m pip install requests')
   sys.exit()

from lib.dork import search_engine as _seg
from lib.tmp import *
from lib.sqlscan import sqli_scan

_x = datetime.datetime.now()
__ = []

class search_engine(_seg):

       def __init__(
                    self,
                    dork,
                    page,
                    proxy=None
                    ):
          super().__init__(
                           dork,
                           page,
                           proxy=None
                           )
        
          for a in super().google:
              __.append(a)
              print(a)
          for b in super().bing:
              __.append(b)
              print(b)
          for c in super().yahoo:
              __.append(c)
              print(c)
          for d in super().baidu:
              __.append(d)
              print(d)

class SQLi_scanner(sqli_scan):
      pass


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
try:
    if arg.scan:
       if arg.key != None or arg.max_page != None:
          print(logo)
          search_engine(arg.key,arg.max_page,proxy=arg.proxy)
          for i in __:
              SQLi_scanner().scan(i)
       else:
          par.print_help()
    elif not arg.scan:
         if arg.key != None and arg.max_page != None:
            print(logo)
            search_engine(arg.key,arg.max_page,proxy=arg.proxy)
         else:
            par.print_help()
    else:
       par.print_help()
except Exception as e:
    print(e)
except KeyboardInterrupt:
    sys.exit('Stop....')
