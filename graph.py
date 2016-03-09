#encoding=utf-8
from matplotlib import pyplot
import MySQLdb
import numpy
import chardet
import string
import sys

reload(sys)
sys.setdefaultencoding('utf8')
con=MySQLdb.connect(host='127.0.0.1',port=8889,user='root',passwd='root',db='mysql',charset='utf8')
cur=con.cursor()

def authorPy():
    cur.execute("SELECT * FROM author ORDER BY frequency DESC")
    author=cur.fetchmany(10)
    x=range(1,11,1)
    y=[]
    xticks=[]
    xaxit=0.9
    for i in author:
        y.append(i[1])
        yaxit=i[1]+0.1
        pyplot.text(xaxit,yaxit,i[1])
        xaxit+=1
        xticks.append(i[0])
    pyplot.xlim(0,11)
    pyplot.xlabel('Authors')
    pyplot.title('Top 10 Author')
    pyplot.ylabel('Number')
    pyplot.bar(x,y,0.5,align='center',color='g',alpha=.5)
    pyplot.xticks(numpy.linspace(1,10,10),xticks)
    pyplot.show()

def hourPy():
    cur.execute("SELECT * FROM time_hour ORDER BY hour")
    x=range(0,25,1)
    y=[]
    xaxit=0
    for i in cur.fetchall():
        y.append(i[1])
        yaxit=i[1]+0.1
        pyplot.text(xaxit,yaxit,i[1])
        xaxit+=1
    y.append(0)
    pyplot.xlim(0,24)
    pyplot.bar(x,y,alpha=.5,align='center')
    pyplot.xticks(numpy.linspace(-1,23,25))
    pyplot.title("Number of posts over time")
    pyplot.xlabel("Hour")
    pyplot.ylabel("Number")
    pyplot.show()

def week():
    x=range(0,7,1)
    y=[91,115,111,77,86,114,112]
    xaxit=0
    xticks=['Sun',"Mon","Tue","Wed","Thu",'Fri',"Sat"]
    for i in y:
        pyplot.text(xaxit,i+1,i)
        xaxit+=1
    pyplot.xlabel("Week")
    pyplot.ylabel("Post")
    pyplot.title("Number of Post Over Time")
    pyplot.bar(x,y,alpha=.5,align='center',color='c')
    pyplot.xticks(numpy.linspace(0,6,7),xticks)
    pyplot.show()

def forum():
    cur.execute("SELECT * FROM forum ORDER BY frequency DESC")
    x=range(0,10,1)
    y=[]
    xticks=[]
    xaxit=0
    for i in cur.fetchmany(10):
        y.append(i[1])
        xticks.append(i[0])
        pyplot.text(xaxit,i[1]+1,i[1])
        xaxit+=1
    pyplot.title("Top 10 Module")
    pyplot.xlabel("Module")
    pyplot.ylabel("Number of Posts")
    pyplot.bar(x,y,alpha=.5,align='center',color='y')
    pyplot.xticks(numpy.linspace(0,9,10),xticks)
    pyplot.show()

def followMost():
    cur.execute("SELECT * FROM follow ORDER BY follow DESC")
    pyplot.rcParams['font.sans-serif'] = ['FangSong']
    x=range(1,11,1)
    y=[]
    xticks=[]
    xaxit=1
    for i in cur.fetchmany(10):
        y.append(i[1])
        str=i[0]
        str=str.encode(encoding='utf8')
        xticks.append(i[0])
        pyplot.text(xaxit,i[1]+1,i[1])
        pyplot.text(xaxit,i[1]-2,i[0],rotation='vertical',fontsize=15)
        xaxit+=1
    pyplot.ylim(0,95)
    pyplot.title("Top 10 Follow")
    pyplot.ylabel("Number of follow")
    pyplot.xlabel("Post")
    pyplot.bar(x,y,alpha=.5,align='center',color='m')
    pyplot.xticks(numpy.linspace(0,10,11))
    pyplot.show()

def followLast():
    cur.execute("SELECT * FROM follow ORDER BY follow")
    pyplot.rcParams['font.sans-serif'] = ['FangSong']
    x=range(1,11,1)
    y=[]
    xticks=[]
    xaxit=1
    for i in cur.fetchmany(10):
        y.append(i[1])
        str=i[0]
        str=str.encode(encoding='utf8').strip()
        xticks.append(i[0])
        pyplot.text(xaxit,i[1]+0.1,i[1])
        pyplot.text(xaxit,i[1]-0.05,i[0],rotation='vertical',fontsize=15)
        xaxit+=1
    pyplot.ylim(0,3)
    pyplot.title("The Last 10 Follow")
    pyplot.ylabel("Number of follow")
    pyplot.xlabel("Post")
    pyplot.bar(x,y,alpha=.3,align='center',color='r')
    pyplot.xticks(numpy.linspace(1,10,10))
    pyplot.show()

def location():
    cur.execute("SELECT * FROM ns ORDER BY frequency DESC ")
    pyplot.rcParams['font.sans-serif'] = ['FangSong']
    x=range(1,11,1)
    y=[]
    xticks=[]
    xaxit=1
    for i in cur.fetchmany(10):
        y.append(i[1])
        str=i[0]
        str=str.encode(encoding='utf8').strip()
        xticks.append(i[0])
        pyplot.text(xaxit,i[1]+0.1,i[1])
        xaxit+=1
    pyplot.ylim(0,25)
    pyplot.title("Top 10 Loaction")
    pyplot.ylabel("Frequency")
    pyplot.xlabel("Location")
    pyplot.bar(x,y,alpha=.3,align='center',color='m')
    pyplot.xticks(numpy.linspace(1,10,10),xticks)
    pyplot.show()

def person():
    cur.execute("SELECT * FROM nh ORDER BY frequency DESC ")
    pyplot.rcParams['font.sans-serif'] = ['FangSong']
    x=range(1,11,1)
    y=[]
    xticks=[]
    xaxit=1
    for i in cur.fetchmany(10):
        y.append(i[1])
        str=i[0]
        str=str.encode(encoding='utf8').strip()
        xticks.append(i[0])
        pyplot.text(xaxit,i[1]+0.1,i[1])
        xaxit+=1
    pyplot.ylim(0,7)
    pyplot.title("Top 10 Person Name")
    pyplot.ylabel("Frequency")
    pyplot.xlabel("Name")
    pyplot.bar(x,y,alpha=.3,align='center',color='m')
    pyplot.xticks(numpy.linspace(1,10,10),xticks)
    pyplot.show()

def sports():
    cur.execute('''SELECT * FROM(SELECT * FROM (SELECT * FROM j ORDER BY frequency DESC)AS noun1 UNION ALL SELECT * FROM(SELECT * FROM nz ORDER BY frequency DESC )AS noun2)AS noun3 ORDER BY frequency DESC''')
    pyplot.rcParams['font.sans-serif'] = ['FangSong']
    data={}
    for i in cur.fetchall():
        if i[0] in data:
            data[i[0]]+=i[1]
        else:
            data[i[0]]=i[1]
    data_list=[]
    for i in data.items():
        str=i[0]
        data_list.append((i[1],str))
    data_list.sort(reverse=True)
    x=range(1,11,1)
    y=[]
    xticks=[]
    xaxit=1
    for i in range(10):
        y.append(data_list[i][0])
        str=data_list[i][1]
        str=str.encode(encoding='utf8')
        xticks.append(str)
        pyplot.text(xaxit,data_list[i][0]+0.1,data_list[i][0])
        xaxit+=1
    pyplot.ylim(0,12)
    pyplot.title("Top 10 Sport Word")
    pyplot.xlabel("Word")
    pyplot.ylabel("Frequency")
    pyplot.bar(x,y,align='center',alpha=.5)
    pyplot.xticks(numpy.linspace(1,10,10),xticks)
    pyplot.show()

def english():
    cur.execute("SELECT * FROM ws ORDER BY frequency DESC ")
    x=range(1,11,1)
    y=[]
    xticks=[]
    xaxit=1
    for i in cur.fetchmany(10):
        y.append(i[1])
        str=i[0]
        str=str.encode(encoding='utf8').strip()
        xticks.append(i[0])
        pyplot.text(xaxit,i[1]+0.1,i[1])
        xaxit+=1
    pyplot.ylim(0,25)
    pyplot.title("Top 10 English Word")
    pyplot.ylabel("Frequency")
    pyplot.xlabel("Word")
    pyplot.bar(x,y,alpha=.3,align='center',color='m')
    pyplot.xticks(numpy.linspace(1,10,10),xticks)
    pyplot.show()