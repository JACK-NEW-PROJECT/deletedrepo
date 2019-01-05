#-*- coding: utf-8 -*-
import sys, time
class color:
      if sys.platform in ["linux", "linux2"]:
         green = '\033[92m'
         red = '\033[91m'     
         white = '\033[0m'
         blue = '\033[94m'
         yellow = '\033[93m'
         IJO_ANU = '\033[35;5;92m'
      else:
         green = ''
         red = ''
         white = ''
         blue = ''
         yellow = ''
         IJO_ANU = ''

logo=("""%s
   _     _        _______ _____ _______ _______ _______ _______
   |     | |         |      |   |  |  | |_____|    |    |______
   |_____| |_____    |    __|__ |  |  | |     |    |    |______
                 ______   _____   ______ _     _
                 |     \ |     | |_____/ |____/
                 |_____/ |_____| |    \_ |    \_%s INDONESIAN PEOPLE

                  %sCODENAME%s : JAXbcd
                  %sTEAM%s : 407 Autehntic Exploit
                  %sCONTACT%s : fb.me/jaka.lesmana.794628
""") % (color.IJO_ANU, color.white,color.yellow,color.white,color.yellow,color.white,color.yellow,color.white)

def INF(em):
    for tx in em + '\n':
        sys.stdout.write(tx)
        sys.stdout.flush()
        time.sleep(3./90)


