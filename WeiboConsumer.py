#!/usr/bin/python
# coding:utf-8

__author__ = 'Sun'

import sys
import re
import os
import urllib2
import urllib
import threading
import hashlib
from Queue import Queue
from bs4 import BeautifulSoup
from MysqlUtil import MysqlUtil 
reload(sys) 
sys.setdefaultencoding('utf-8')

class WeiboConsumer(threading.Thread):
	def __init__(self,t_name,queue):
		threading.Thread.__init__(self, name = t_name)
		self.user_queue = queue

	def run(self):
		cookie = 'set yourself login cookie'
		headers = {
			'User-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
			'cookie': cookie
		}
		mysql_client = MysqlUtil('10.1.3.42','root','root','weibo_rss','utf8')
		while True:
			try:
				self.userid = self.user_queue.get(1,20)
				print self.getName() + 'start working: ' + self.userid
				url = 'http://weibo.cn/' + self.userid
				
				request = urllib2.Request(url, headers = headers)
				data = urllib2.urlopen(request).read()
				soup = BeautifulSoup(data)
				content = soup.find_all(attrs={'class': 'c'})
				username = soup.find(attrs={'class': 'ut'})
				username = username.find(attrs={'class':'ctt'})
				self.username = username.stripped_strings.next()
				for item in content:
					if item.has_attr('id'):
						data_id = item['id']
					else:
						continue
					data =  str(item)
					# save to mysql
					self.saveToMysql(mysql_client,data,data_id)					
			except Exception, e:
				print self.getName() + ' finished!'
				break
		mysql_client.close()

	def saveToMysql(self,mysql_client,text,text_id):
	    sql = 'insert into weibo_content(weibo_userid,weibo_username,content,content_id) select %s,%s,%s,%s from dual where not exists (select * from weibo_content where content_id=%s)'
            param = (self.userid,self.username,text,text_id,text_id)
	    mysql_client.insert(sql,param)

#if __name__ == '__main__':
#	queue = Queue(200)
#	queue.put('fbb0916')
#	consumer = Consumer('Consumer_1', queue)
#	consumer.start()


