#coding=utf-8
import bbs_top10
import time
import hotword
<<<<<<< HEAD
import logging


while True:
    cre=bbs_top10.crawler()
    cre.run()
    print( ''' wait for next crawler and sleep for 1800s
##############################################################################
    ''')
=======
import subprocess

while True:
    subprocess.Popen('cmd python hotword.py',shell=True)
    cre=bbs_top10.crawler()
    cre.run()
    print ''' wait for next crawler and sleep for 1800s
##############################################################################
    '''
>>>>>>> 91ac9e3ebc8f7d34b1106636e14cae53662cf618
    time.sleep(1800)
