#-*- coding: utf-8 -*-
import requests, re, sys
try:
   from urllib.parse import unquote
except ImportError:
   from urllib2 import unquote
from tmp.temp import color, INF


GOOGLE = color.yellow+"!INFO"+color.green+" : SEARCH TO  www.google.com"+color.white
BING =   color.yellow+"!INFO"+color.green+" : SEARCH TO  www.bing.com"+color.white
DUCK =   color.yellow+"!INFO"+color.green+" : SEARCH TO  www.duckduckgo.com"+color.white
YAHOO =  color.yellow+"!INFO"+color.green+" : SEARCH TO  www.search.yahoo.com"+color.white

def dork(dork, page=None):
    list_url = []
    bing_url = 'https://www.bing.com/search'
    google_url = 'https://www.google.com.sg/search'
    duck_url = 'https://duckduckgo.com/html'
    yahoo_search_url = 'https://search.yahoo.com/search'
    try:
        for cok in range(1,(page+1)):
            start = '&first={}'.format(str((cok-1)*10))
            bing_query = '{}?q={}{}'.format(bing_url,dork,start)
            bing_response = requests.get(bing_query, timeout=5,  allow_redirects=True).text
            urls = re.findall('<h2><a href="(.+?)" h=',bing_response)
            for i in range(len(urls)):
                list_url.append(urls[i])
    except requests.exceptions.ConnectionError:
        print(color.red+"[!] Bing No Internet Connection [!]\n"+color.white)
    except requests.exceptions.ConnectTimeout:
        print(color.red+"[!] Bing Connections Time Out [!]\n"+color.white)
    except requests.exceptions.ReadTimeout:
        print(color.red+"[!] Bing Connection Time out [!]"+color.white)
    except KeyboardInterrupt:
        sys.exit()

    try:
        INF(BING)
        INF(GOOGLE)
        for cok in range(1,(page+1)):
            start = "&start={}".format(str((cok-1)*10))
            google_query = "{}?q={}{}".format(google_url,dork,start)
            google_response = requests.get(google_query, allow_redirects=True, timeout=5).content
            link_google = unquote(str(google_response))
            url = re.findall('class="r"><a href="/url\?q=(.*?)&amp', link_google)
            for i in range(len(url)):
                list_url.append(url[i])
    except requests.exceptions.ConnectionError:
        print(color.red+"[!] Google No Internet Connections [!]\n"+color.white)
    except requests.exceptions.ConnectTimeout:
        print(color.red+"[!] Google Connections Time Out [!]\n"+color.white)
    except requests.exceptions.ReadTimeout:
        print(color.red+"[!] Google Connection Time out [!]"+color.white)
    except KeyboardInterrupt:
        sys.exit()

    try:
        INF(DUCK)
        for cok in range(1,(page+1)):
            duck_query = "{}?q={}".format(duck_url,dork)
            duck_response = requests.get(duck_query,  allow_redirects=True, timeout=2).content
            link_url = unquote(str(duck_response))
            url = re.findall('class="result__url" href="/l/\?kh=-1&amp;uddg=(.*?)">',link_url)
            for i in range(len(url)):
                list_url.append(url[i])
    except requests.exceptions.ConnectionError:
        print(color.red+"[!] Duck No Internet Connections [!]\n"+color.white)
    except requests.exceptions.ConnectTimeout:
        print(color.red+"[!] Duck Connection Time out [!]\n"+color.white)
    except requests.exceptions.ReadTimeout:
        print(color.red+"[!] Duck Connection Time out [!]"+color.white)
    except KeyboardInterrupt:
        sys.exit()

    try:
        INF(YAHOO)
        for cok in range(1, (page+1)):
            start = "&b={}".format(str((cok-1)*10))
            yahoo_query = "{}?p={}{}".format(yahoo_search_url,dork,start)
            yahoo_response = requests.get(yahoo_query, allow_redirects=True, timeout=5).content
            links_yahoo = unquote(str(yahoo_response))
            yahoo_list = re.findall('class=" ac-algo fz-l ac-21th lh-24" href="(.*?)"', links_yahoo)
            for i in range(len(yahoo_list)):
                list_url.append(yahoo_list[i])
    except requests.exceptions.ConnectionError:
        print(color.red+"[!] Yahoo No Internet Connections [!]"+color.white)
    except requests.exceptions.ConnectTimeout:
        print(color.red+"[!] Yahoo Connection Time out [!]"+color.white)
    except requests.exceptions.ReadTimeout:
        print(color.red+"[!] Yahoo Connection Time out [!]"+color.white)
    except KeyboardInterrupt:
        sys.exit()
    return list_url






