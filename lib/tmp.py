#-*- coding: utf-8 -*-
import sys

if sys.platform in ['linux','linux2']:
   W = '\033[0m'
   G = '\033[92m'
   R = '\033[91m'
   B = '\033[94m'
   Y = '\033[93m'
   Z ='\033[35;5;92m'

else:
   W = ''
   G = ''
   R = ''
   B = ''
   Y = ''
   Z = ''


logo = '''{}
   _     _        _______ _____ _______ _______ _______ _______
   |     | |         |      |   |  |  | |_____|    |    |______
   |_____| |_____    |    __|__ |  |  | |     |    |    |______
                 ______   _____   ______ _     _
                 |     \ |     | |_____/ |____/
                 |_____/ |_____| |    \_ |    \_{} INDONESIAN PEOPLE
                                                       [v] : {}4.0{}

                 {}BY{} : 407 AUTHENTIC EXPLOIT
                 {}Codename{} : JaxBCD
                 {}Contact{} : fb.me/jaka.lesmana.794628

        '''.format(Z,W,B,W,Y,W,Y,W,Y,W)
