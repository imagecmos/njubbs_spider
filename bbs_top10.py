#coding=utf-8
import urllib2
from bs4 import BeautifulSoup
import os,sys,time
import MySQLdb
import re
import requests
import logging

class crawler:
    def __init__(self):
        self.logger=logging.getLogger()
        self.hander=logging.StreamHandler()
        self.formate=logging.Formatter('%(asctime)s-----%(processName)s----%(message)s)')
        self.hander.setFormatter(self.formate)
        self.logger.addHandler(self.hander)
        self.logger.setLevel(logging.INFO)
        self.url=r"http://bbs.nju.edu.cn/bbstop10"
        self.save_html_path=r"D:\TaotaoCao\spider\html"

    #make dir for save the html in formar:year_month_day
    def make_tody_html_dir(self):
        time_tody=time.gmtime()
        year=time_tody.tm_year
        month=time_tody.tm_mon
        tody=time_tody.tm_mday
        self.save_html_path+="\\"+repr(year)+"_"+repr(month)+"_"+repr(tody)
        if not os.path.exists(self.save_html_path):
            os.makedirs(self.save_html_path)


    #get the data and insert into db
    def run(self):
        request=requests.get(r"http://bbs.nju.edu.cn/bbstop10")
        text=request.text
        soup=BeautifulSoup(text,'lxml',from_encoding='gb2312')
        tr=soup.table.find_all(['tr'])

        insert=list()
        for i in tr[1:]:
            one_tr=i.find_all(['td'])
            for td in one_tr:
                insert.append(td.string.strip().encode('utf-8'))

        td_all=soup.find_all('td')
        time_list=list()
        for i in td_all:
            if i.a!=None:
                u=i.a["href"]
                m=re.search(r"M\.\w+\.A",u)
                if m:
                    title_url=r"http://bbs.nju.edu.cn/"+u
                    title_request=requests.get(title_url)
                    title_soup=BeautifulSoup(title_request.text,"lxml",from_encoding="gdb2312")
                    try:
                        body=title_soup.textarea.string.encode("utf-8")
                    except Exception as e:
                        time_list.append("pass")
                        continue
                    m=re.search("(?<=南京大学小百合站 \().+(?=\))",body)
                    if m:
                        post_title_time=m.group(0)
                        time_list.append(post_title_time)
                        time.sleep(1)

        index=0
        for i in [5,11,17,23,29,35,41,47,53,59]:
            insert.insert(i,time_list[index])
            index+=1

        new_insert=list()
        for i in range(0,60,6):
            a=insert[i:i+6]
            new_insert.append(a)

        con=MySQLdb.connect(host="127.0.0.1",port=8889,user="root",passwd="root",db="mysql",charset="utf8")
        cur=con.cursor()
        for line in new_insert:
            rank,forum,title,author,follow,title_time=line
            sql="INSERT INTO bbs VALUES('%s','%s','%s','%s','%s','%s')"%(rank,forum,title,author,follow,title_time)
            result=cur.execute(sql)
            if result!=1:
                self.logger.info(rank+" "+forum+" "+title+" "+author+" "+forum+" "+"insert error")
                con.rollback()
                continue
            con.commit()
        cur.close()
        con.close()

        pre=soup.prettify(encoding="utf-8")
        time_now=time.gmtime()
        hour_now=repr(time_now.tm_hour)
        min_now=repr(time_now.tm_min)
        file_name=hour_now+"_"+min_now+".html"
        self.make_tody_html_dir()
        file=open(self.save_html_path+"\\"+file_name,'w+')
        try:
            file.write(pre)
        except Exception as e:
            self.logger.info("write html source into file error")

