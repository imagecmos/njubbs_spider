#coding=utf-8
import bbs_top10
import time
import hotword
import subprocess

while True:
    subprocess.Popen('cmd python hotword.py',shell=True)
    cre=bbs_top10.crawler()
    cre.run()
    print ''' wait for next crawler and sleep for 1800s
##############################################################################
    '''
    time.sleep(1800)
