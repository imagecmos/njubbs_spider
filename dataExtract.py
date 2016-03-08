#encoding=utf-8
import MySQLdb
import re
import os
import shutil
import urllib2
import chardet

path=r"C:\Users\imagecmos\Desktop\spider_data"
dataPath=r"C:\Users\imagecmos\Desktop\spider_data"

con=MySQLdb.connect(host="127.0.0.7",user="root",passwd="root",port=8889,db="mysql",charset='utf8')
cur=con.cursor()

#split sentence
def get_key(text):
    url_get_base="http://ltpapi.voicecloud.cn/analysis/?"
    api_key="e10465w7O4R0J2R0q745ZQ7GzvvhNxeAPyDMbd2N"
    format="plain"
    pattern="pos"
    result=urllib2.urlopen("%sapi_key=%s&text=%s&format=%s&pattern=%s"%(url_get_base,api_key,text,format,pattern))
    content=result.read().strip()
    return content

#class word
def result(content):
    content=content.split(' ')
    for i in content:
        if "wp" in i:
            continue
        i=i.split("_")
        _path=os.path.join(path,i[1]+".txt")
        if os.path.exists(_path):
            file=open(_path,'a+')
            file.write(i[0]+"\n")
        else:
            file=open(_path,"w")
            file.write(i[0]+"\n")

#insert into mysql
def insSQL(path):
    tag=os.path.basename(path)
    tag=os.path.splitext(tag)[0]
    cur.execute('''CREATE TABLE %s(
word VARCHAR(20) NOT NULL PRIMARY KEY,
frequency INT NOT NULL
)CHARSET=utf8'''%tag)
    con.commit()
    file=open(path,'r')
    lines=file.readlines()
    for line in lines:
        line=line.strip('\n').strip()
        try:
            cur.execute("SELECT word,frequency FROM %s WHERE word='%s'"%(tag,line))
            if cur.rowcount:
                num=cur.fetchone()[1]+1
                cur.execute("UPDATE %s SET frequency=%d WHERE word='%s'"%(tag,num,line))
            else:
                cur.execute("INSERT INTO %s VALUES('%s',1)"%(tag,line))
            con.commit()
        except Exception,e:
            print e
            cur.execute("DROP TABLE %s"%(tag))
            con.commit()
            exit(0)
    file.close()

#creat follow table
def follow():
    cur.execute('''CREATE TABLE follow(
    title VARCHAR(100) NOT NULL PRIMARY KEY,
    follow INT NOT NULL,
    title_time VARCHAR(50) NOT NULL
    )CHARSET=utf8''')
    con.commit()
    cur.execute("SELECT DISTINCT title FROM bbs_copy ")
    titleData=cur.fetchall()
    for i in titleData:
        i=i[0]
        i=i.encode(encoding='utf-8')
        cur.execute("SELECT MAX(follow),title_time FROM bbs_copy WHERE title='%s'"%(i))
        one=cur.fetchone()
        cur.execute("INSERT INTO follow VALUES('%s',%d,'%s')"%(i,int(one[0]),one[1].encode(encoding='utf-8')))
    con.commit()

if __name__=="__main__":
    cur.execute("SELECT DISTINCT title FROM bbs_copy")
    for i in cur.fetchall():
        i=i[0]
        i=i.encode(encoding='utf8')
        title=get_key(i)
        result(title)
    listPath=os.listdir(dataPath)
    for i in listPath:
        i=os.path.join(dataPath,i)
        insSQL(i)
    follow()



