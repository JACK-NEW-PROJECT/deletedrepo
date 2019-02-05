#-*- coding: utf-8 -*-
import requests,re,sys
from sqlerror import sql_errors

class sqlscan:

      def __init__(self,url):
          self.url = url

      @property
      def scan(self):
          vuln = 0
          res = requests.get(self.url+"'").content
          for typ,error in sql_errors.items():
              if re.search(error, str(res)):
                 vuln += 1
                 print('Error : '+error)
                 print('Type  : '+typ)
              else:
                 pass

          if vuln > 0:
             print("Vulnerability\n")
          else:
             print("\nNot Vulnerability\n")





