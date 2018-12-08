#!/usr/bin/python2.7   #
# -*- coding: utf-8 -*-#
########################
import argparse, requests, re, time, random, sys, colorama
from bs4 import BeautifulSoup as bs
from pygoogling.googling import GoogleSearch as gs
from urllib2 import unquote
parser = argparse.ArgumentParser(prog='python2 ultimate_dork.py', add_help=True)
parser = argparse.ArgumentParser(description='Ultimate Tool Dork Search')
parser.add_argument("-d", '--dork', help="Your dork  to Input Use String Type e.g inurl:index,of")
parser.add_argument("-v", '--verbose',  help="with Verbosity", action='store_true')
parser.add_argument("-p", '--proxy',  help="if Using Proxy IP:port")
parser.add_argument("-o", '--output',  help="Output Save File")
parser.add_argument('--nobanner',  action='store_false', help="Dont Show Banner")
parser.add_argument('--version', action='version', version='%(prog)s 1.0 Version')
args = parser.parse_args()
##
tinky = ' [+]'
winky = ' [!]\n'
dipsy = ' [x]\n'
lala = ' [-]\n'
poo = ' [*]'
col = colorama.Fore
blue = col.BLUE
green = col.GREEN
red = col.RED
yellow = col.YELLOW
cyan = col.CYAN
Lmagenta = col.LIGHTMAGENTA_EX
bright = colorama.Style.DIM
Lred = col.LIGHTRED_EX
Lgreen = col.LIGHTGREEN_EX
Lyellow = col.LIGHTYELLOW_EX
_white = col.WHITE
ERROR = Lred+' Connection Error'+winky+_white
TIME_OUT = Lred+'Connection Error'+winky+_white
ERROR_CODE = Lred+'Status Respone Error Code'+winky+_white
INV_ = Lred+'Invalid Url'+lala+_white
STTS = green+' Status : '+_white
DEC_ERROR = Lred+' Content Error'+winky+_white

##
bobo = time.sleep
c = args.dork
no_ban = args.nobanner
output = args.output
verbose = args.verbose
proxy = args.proxy
query = c
bing_count = random.randint(0, 20)
bing_query = { 'q': query,'first':'0','count':int(bing_count)*10+1 }
duck_query = {'q':c}
ask_query = {'q':query, 'page':bing_count}
prox = { 'http' : proxy }
header = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
          'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
       	  'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
	  'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
	  'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
	  'Microsoft Internet Explorer/4.0b1 (Windows 95)',
	  'Opera/8.00 (Windows NT 5.1; U; en)',
	  'amaya/9.51 libwww/5.4.0',
	  'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
	  'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
	  'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
	  'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
 	  'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
 	  'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]',
          'Mozilla/5.0 (Linux; Android 5.1.1; SM-N750K Build/LMY47X; ko-kr) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Puffin/6.0.8.15804AP',
          'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
          'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) OPiOS/10.2.0.93022 Mobile/11D257 Safari/9537.53',
          'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) FxiOS/7.5b3349 Mobile/14F89 Safari/603.2.4']

ag = random.choice(header)
headers = { 'User-agent' : ag }
try:
   if output:
      asede = open(output, 'a+')
   else:
      asede = open('results.txt', 'a+')
except NameError:
   parser.print_help
   print Lred+lala+'Please Using Output --output'+lala+_white
except TypeError:
   parser.print_help
   print Lred+lala+'Please Using Output --output'+lala+_white
   sys.exit()
def dork_():
    print yellow+poo+_white+Lgreen+'Searching... In Google.com'+_white
    try:
       G = gs(query)
      # print yellow+poo+_white+Lgreen+'Searching... In Google.com'+_white
       ciyee_recode = G.start_search(max_page=bing_count)
       oh = G.search_result
       if not verbose:
          for u in oh:
              print blue,tinky,_white,u,_white
              print u
              #asede.write(u+'\n')

       else:
          for u in oh:
                 try:
                    req = requests.get(u, headers=headers, timeout=10)
                    print blue,tinky,_white,u,_white,STTS,req
                    #asede.write(u+'\n')
                 except requests.exceptions.ConnectionError:
                    print ERROR
                 except requests.exceptions.ReadTimeout:
                    print TIME_OUT
                 except requests.exceptions.TooManyRedirects:
                    print ERROR_CODE
                 except requests.exceptions.MissingSchema:
                    print INV_
                 except requests.exceptions.ContentDecodingError:
                    print DEC_ERROR
                 except requests.exceptions.InvalidURL:
                    print INV_
                 except:
                    print Lred+'Connection Broken [!]'+_white
       url2 = 'https://www.bing.com/search'
       print yellow+poo+_white+Lgreen+'Searching... In Bing.com'+_white
       r = requests.get(url2, params=bing_query, headers=headers, proxies=prox,allow_redirects=True, timeout=15)
       sop = bs(r.text, "html.parser")
       tag = sop.find_all('h2')
       if not verbose:
          for ez in tag:
              ze = ez.find_all('a')
              for bingung_w in ze:
                  njipik = bingung_w.get('href')
                  asede.write(njipik+'\n')

                  print blue,tinky,_white,njipik,_white
       else:
          for ez in tag:
              ze = ez.find_all('a')
              for bingung_w in ze:
                  njipik = bingung_w.get('href')
                  asede.write(njipik+'\n')
                  try:
                     req = requests.get(njipik, headers=headers, timeout=5)
                     print blue,tinky,_white,njipik,_white,STTS,req
                  except requests.exceptions.ConnectionError:
                     print ERROR
                  except requests.exceptions.ReadTimeout:
                     print TIME_OUT
                  except requests.exceptions.TooManyRedirects:
                     print ERROR_CODE
                  except requests.exceptions.MissingSchema:
                     print INV_
                  except requests.exceptions.ContentDecodingError:
                     print DEC_ERROR
                  except requests.exceptions.InvalidURL:
                     print INV_
                  except:
                     print Lred+'Connection Broken [!]'+_white
       url3 = 'https://duckduckgo.com/html'
       print yellow+poo+_white+Lgreen+'Searching... In DuckDuckGo.com'+_white
       r = requests.get(url3, params=duck_query, headers=headers, proxies=prox,allow_redirects=True,  timeout=15)
       sop = bs(r.text, 'html.parser')
       oi = sop.find_all('a', class_='result__url')
       if not verbose:
          for st in oi:
               parkir = st.get('href')
               hai = unquote(parkir[15:])
               print blue,tinky,_white,hai,_white
               asede.write(hai+'\n')
       else:
          for st in oi:
              parkir = st.get('href')
              wek = unquote(parkir[15:])
              asede.write(wek+'\n')
              try:
                  req = requests.get(wek, headers=headers, timeout=5)
                  print blue,tinky,_white,wek,_white,STTS,req
              except requests.exceptions.ConnectionError:
                  print ERROR
              except requests.exceptions.ReadTimeout:
                  print TIME_OUT
              except requests.exceptions.TooManyRedirects:
                  print ERROR_CODE
              except requests.exceptions.MissingSchema:
                  print INV_
              except requests.exceptions.ContentDecodingError:
                  print DEC_ERROR
              except requests.exceptions.InvalidURL:
                  print INV_
              except:
                 print Lred+'Connection Broken [!]'+_white
       url4 = 'https://www.search.ask.com/web'
       print yellow+poo+_white+Lgreen+'Searching... In Ask.com'+_white
       r = requests.get(url4, params=ask_query, headers=headers, proxies=prox,allow_redirects=True, timeout=15)
       sop = bs(r.text, 'html.parser')
       em = sop.find_all('a', class_="algo-title")
       if not verbose:
          for i in em:
              vos = i.get('href')
              asede.write(vos+'\n')
              print blue,tinky,_white,vos,_white
       else:
          for i in em:
              vos = i.get('href')
              try:
                  req = requests.get(vos, headers=headers, timeout=5)
                  print blue,tinky,_white,vos,_white,STTS,req
                  asede.write(vos+'\n')
              except requests.exceptions.ConnectionError:
                  print ERROR
              except requests.exceptions.ReadTimeout:
                  print TIME_OUT
              except requests.exceptions.TooManyRedirects:
                  print ERROR_CODE
              except requests.exceptions.MissingSchema:
                  print INV_
              except requests.exceptions.ContentDecodingError:
                  print DEC_ERROR
              except requests.exceptions.InvalidURL:
                  print INV_
              except:
                 print Lred+'Connection Broken [!]'+_white
       url5 = 'https://search.yahoo.com/search?p='+query
       print yellow+poo+_white+Lgreen+'Searching... In Yahoo.com'+_white
       r = requests.get(url5, headers=headers, proxies=prox,allow_redirects=True, timeout=15)
       pft  = bs(r.text, 'html.parser').find_all('a', class_=" ac-algo fz-l ac-21th lh-24")
       if not verbose:
          for mek in pft:
              ng = mek.get('href')
              asede.write(ng+'\n')
              print blue,tinky,_white,ng,_white
       else:
          for mek in pft:
              ng = mek.get('href')
              asede.write(ng+'\n')
              try:
                 req = requests.get(ng, headers=headers, timeout=5)
                 print blue,tinky,_white,ng,_white,STTS,req
                 asede.write(ng+'\n')
              except requests.exceptions.ConnectionError:
                  print ERROR
              except requests.exceptions.ReadTimeout:
                  print TIME_OUT
              except requests.exceptions.TooManyRedirects:
                  print ERROR_CODE
              except requests.exceptions.MissingSchema:
                  print INV_
              except requests.exceptions.ContentDecodingError:
                  print DEC_ERROR
              except requests.exceptions.InvalidURL:
                  print INV_
              except:
                 print Lred+'Connection Broken [!]'+_white
       if output:
          print Lgreen+tinky+magenta+'Your File Save To'+output+Lgreen+tinky+_white
          asede.close
       else:
          print Lgreen+tinky+magenta+'Your File Save To results.txt'+Lgreen+tinky+_white
          asede.close
    except UnboundLocalError:
        parser.print_help()
    except AttributeError:
        parser.print_help()
    except KeyboardInterrupt:
        print red+'Aborted'+dipsy+_white
    except NameError:
        parser.print_help





def logo():
    print  """%s
   _     _        _______ _____ _______ _______ _______ _______
   |     | |         |      |   |  |  | |_____|    |    |______
   |_____| |_____    |    __|__ |  |  | |     |    |    |______
                 ______   _____   ______ _     _
                 |     \ |     | |_____/ |____/
                 |_____/ |_____| |    \_ |    \_%s

       %s{+}----{%s Author  : JaxBCD                %s}----{+}%s
       %s{+}----{%s Contact : fb.me/jack.lesmen.5   %s}----{+}%s
       %s{+}----{%s Team    : 407 Authentic Exploit %s}----{+}%s
""" % (cyan, _white, Lgreen, Lyellow, Lgreen, Lyellow, Lgreen, Lyellow, Lgreen, Lyellow, 
       Lgreen, Lyellow, Lgreen, _white)

if __name__ == '__main__':
   if not no_ban:
      dork_()
   else:
      logo()
      dork_()

