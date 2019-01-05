# SUPPORT PYTHON VERSION : 2.7.x and 3.7.x
#-*- coding: utf-8 -*-
# COPYRIGHT©2019 https://github.com/jaxBCD
# CONTACT : fb.me/jaka.lesmana.794628
# TEAM : 407 AUTHENTIC EXPLOIT

import sys,argparse, os


from core.dork import dork
from core.sqlscan import scan as SCANNER
from tmp.temp import *

parser = argparse.ArgumentParser(prog='python2 ultimate_dork.py', add_help=True)
parser = argparse.ArgumentParser(description='Ultimate Tool Dorking Url and SQLi scan')
parser.add_argument('--dork', help="Your Dork e.g inurl:.php?id=,intext:ex", type=str)
parser.add_argument('--max-page', help="Max Page Results Search", type=int)
parser.add_argument('--scan', help="Scan SQL injection Vulnerability", action="store_true")
parser.add_argument('--output', help="output save file")
parser.add_argument('--version', action='version', version='%(prog)s 3.0 Version')
args = parser.parse_args()

dorkny = args.dork
maxpage = args.max_page
scan = args.scan
output = args.output
try:
   if scan:
      print(logo)
      for link in dork(dorkny, page=maxpage):
          print(color.blue+'[+] '+color.white+link)
          print("\n\n")
          SCANNER(link).sqli_scan()
          opt = open(output, 'a+')
          opt.write(link + '\n')
          opt.close()

   elif not scan:
        print(logo)
        for link in dork(dorkny, page=maxpage):
            print(color.blue+'[+] '+color.white+link)
            opt = open(output, 'a+')
            opt.write(link + '\n')
            opt.close()

   else:
        parser.print_help()
except KeyboardInterrupt:
   pass
except KeyError:
   parser.print_help()

