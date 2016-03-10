#coding=utf-8
import bbs_top10
import time
import hotword
import logging


while True:
    cre=bbs_top10.crawler()
    cre.run()
    print( ''' wait for next crawler and sleep for 1800s'''+"#"*70)
    time.sleep(1800)
