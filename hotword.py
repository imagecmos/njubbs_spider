#coding=utf8
import MySQLdb
import urllib2
from bs4 import BeautifulSoup
import time
import re
import chardet

url=r"http://top.baidu.com/buzz?b=341&c=513&fr=topbuzz_b341_c513"
def gethot_word(time):
    request=urllib2.urlopen(url)
    soup=BeautifulSoup(request,from_encoding="gb2312")
    c_list=soup.select('.list-title')

    con=MySQLdb.connect(host="127.0.0.1",user="root",passwd="root",db="mysql",charset="utf8")
    cur=con.cursor()
    for i in c_list:
        i=i.string.encode("utf-8")
        cur.execute("INSERT INTO hotword VALUES('%s','%s')"%(time,i))
        con.commit()
    cur.close()
    con.close()


if __name__=="__main__":
    while True:
        time_now=time.ctime()
        if re.search("\d\s20:00:\d\d",time_now):
            gethot_word(time_now)
            print "insert hotword %s"%(time_now)
            time.sleep(85000)


