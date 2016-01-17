#coding=utf-8
import MySQLdb
import mutex
import threading
import time
import bbs_top10
import jieba
import matplotlib.pyplot as plt



ji_list=jieba.cut("在冬日里分出高下",cut_all=False)
for i in ji_list:
    print i

'''
def main():
    global mux
    while True:
        mux.acquire()
        cre=bbs_top10.crawler()
        cre.run()
        print ''' ''' wait for next crawler and sleep for 1800s
##############################################################################
 '''
'''
        mux.release()
        time.sleep(1800)
        '''
'''
def del_row():
    global mux
    while True:
        mux.acquire()
        con=MySQLdb.connect("127.0.0.1","root","root","mysql",charset="utf8")
        cur=con.cursor()
        sql="SELECT * FROM test WHERE name='%s'"%(name)
        cur.execute(sql)
        for n,a in cur.fetchall():
            print n," ",a
            break
        cur.close()
        con.close()
        print "fetch complete"
        mux.release()


if __name__=="__main__":
    mux=threading.Lock()
    main_thread=threading.Thread(target=main)
    del_thread=threading.Thread(target=del_row)
    main_thread.start()
    del_thread.start()
    main_thread.join()
    del_thread.join()

'''


