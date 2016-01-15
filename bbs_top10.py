import urllib2
from bs4 import BeautifulSoup
import os,sys,time
import MySQLdb

class crawler:
    def _init_(self):
        self.url=r"http://bbs.nju.edu.cn/bbstop10"
        self.save_html_path=r"D:\TaotaoCao\spider\html"

    #return time for next crawler
    def time_to_next(self):
        time_now=time.gmtime()
        year=time_now.tm_year
        month=time_now.tm_mon
        today=time_now.mday
        return year,month,today

    #make dir for save the html in formar:year_month_day
    def make_tody_html_dir(self,before_year,before_month,before_day):
        time_tody=time.gmtime()
        year=time_tody.tm_year
        month=time_tody.tm_mon
        tody=time_tody.mday
        if before_year==year and before_month==month and before_day==tody:
            pass
        else:
            self.save_html_path+="\\"+year+"_"+month+"_"+tody
            os.makedirs(self.save_html_path)

    def crawler(self):
        request=urllib2.urlopen(self.url)
        soup=BeautifulSoup(request,"lxml",from_encoding="gb2312")
        n=0
        insert=list()
        for link in soup.find_all(['td']):
            if n<5:
                    n+=1
                    continue
            inner_list=list()
            for str in link.stripped_strings:
                str=str.encode("utf-8")
                inner_list.append(str)
            insert.append(inner_list)
        con=MySQLdb.connect("localhost","root","root","mysql")
        cur=con.cursor()
        for line in insert:
            rank,forum,title,author,follow=line
            sql="INSERT INTO bbs VALUES(%s,%s,%s,%s,%s)"%(rank,forum,title,author,follow)
            result=cur.execute(sql)
            if result!=1:
                print rank,forum,title,author,forum,"insert error"
                con.rollback()
            con.commit()

        pre=soup.prettify(encoding="utf-8")
        time_now=time.gmtime()
        hour_now=time_now.tm_hour
        min_now=time_now.tm_min
        file_name=hour_now+"_"+min_now+".html"
        file=open(self.path+"\\"+file_name,'w+')
        file.write(pre)

