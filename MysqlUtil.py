#!/usr/bin/python
# coding:utf-8

import MySQLdb

class MysqlUtil():
    def __init__(self,ip,username,password,dbname,chset):
	self.conn = MySQLdb.connect(ip,username,password,dbname,charset=chset)
	self.conn.autocommit(1)
	self.cursor = self.conn.cursor()

    def insert(self,sql,param):
	return self.cursor.execute(sql,param)

    def select(self,sql,param=('')):
	self.cursor.execute(sql)
	return self.cursor.fetchall()

    def close(self):
	self.cursor.close()
	self.conn.close()

if __name__ == '__main__':
     print '*****'
#    mysql = MysqlUtil('10.1.3.42','root','root','weibo_rss','utf8')
#    sql = "insert into weibo_user(username,truename,description) values(%s,%s,%s)"
#    params = ('xuezhiqian',u'薛之谦','薛之谦的微博!')
#    n = mysql.insert(sql,params)
#    print 'insert:',n
#    sql = "select * from weibo_user"
#    temp = mysql.select(sql,(''))
#    for row in temp:
#	print row
#	for r in row:
#	    print r
#    mysql.close()

