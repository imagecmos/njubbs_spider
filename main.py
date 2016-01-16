#coding=utf-8
import bbs_top10
import time

while True:
    cre=bbs_top10.crawler()
    cre.run()
    time.sleep(3600)
