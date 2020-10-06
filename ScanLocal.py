# coding: utf-8

import os
import subprocess
import re
import threading
import sys


class Ping(threading.Thread):

    def __init__(self, hostname):
        threading.Thread.__init__(self)
        self.hostname = hostname

    def run(self):
        p = subprocess.Popen(["ping", option, self.hostname], stdout=subprocess.PIPE).stdout.read()
        str = p.decode('cp850')
        r = re.search('ponse', str)
        try:
            if(r.group()):
                print(str)
                print(f"L'adresse {self.hostname} existe!") 
        except:
            print(f"L'addrese {self.hostname} n'existe pas")
            pass

OS = sys.platform
 
option = '-n' if OS != 'win32' else '-a' #Option de commande pour linux ou mac 

for i in range(10):
    hostname = "192.168.1.%i" % (i+1)
    background = Ping(hostname)
    background.start()

