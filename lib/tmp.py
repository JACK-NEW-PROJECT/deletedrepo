#-*- coding: utf-8 -*-
import sys
from time import sleep,localtime

class color(object):
      if sys.platform in ['linux','linux2']:
         R = '\033[91m'
         G = '\033[92m'
         B = '\033[94m'
         Y = '\033[93m'
         W = '\033[0m'
      else:
         R = ''
         G = ''
         B = ''
         Y = ''
         W = ''
         


class logo(color):

      def __init__(self):
          pass

      def __str__(self):
          _ = color
          return f'''
           /\            /\     -{_.G} Ultimate Dork{_.W} -
          /  \  ~  ~  /\/  \_
         /____\({_.R}o{_.W})({_.R}o{_.W})/_/\__    {_.Y} Codename{_.W} : JaxBCD
        /|   /(______)   \ \_   - V  :{_.B} 2.0 compatible {_.W}
       / |  /             \_    - {_.R}By{_.W} : 407 Authentic Exploit
     _/ _|_/                    
          '''
def load():
    _ = localtime()
    x = [
        '|','\\','-','/'
    ]
    for y in x:
        print(f'\r [{y}]',end=' Starting At %s %s-%s-%s%s - %s:%s  ' % (color.G,_[0],_[1],_[2],color.W,_[3],_[4]))
        sys.stdout.flush()
        sleep(0.15)

    
              
    
