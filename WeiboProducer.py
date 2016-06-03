#!/usr/bin/python
# coding:utf-8
__author__ = 'Sun'

import sys
import re
import os
import urllib2
import urllib
import threading
from Queue import Queue
from bs4 import BeautifulSoup
from MysqlUtil import MysqlUtil

class WeiboProducer(threading.Thread):
	def __init__(self, t_name, queue):
		threading.Thread.__init__(self, name = t_name)
		self.user_queue = queue

	def run(self):
		mysql_client = MysqlUtil('10.1.3.42','root','root','weibo_rss','utf8')
		start = 0
		size = 2
		while True:
			sql = 'select weibo_userid from weibo_user limit ' + str(start) + ',' + str(size)
			data =  mysql_client.select(sql)
			if len(data) <= 0:
				break
			for i in range(len(data)):
				self.user_queue.put(data[i][0])
			start =  start + size
		
		mysql_client.close()
		print self.getName() + ' finished!'

#if __name__ == '__main__':
#	queue = Queue(100)	
#	producer = Producer('Producer', queue)
#	producer.start()
