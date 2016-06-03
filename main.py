#!/usr/bin/python
# coding:utf-8
__author__ = 'Sun'
import sys
import time
from Queue import Queue
from WeiboProducer import WeiboProducer
from WeiboConsumer import WeiboConsumer

if __name__ == '__main__':
	thread_num = 1
	for i in range(len(sys.argv)):
		if sys.argv[i] == '-t':
			thread_num = int(sys.argv[i+1])
	
	queue = Queue(100)
	producer = WeiboProducer('Weibo_producer', queue)
	producer.start()
	time.sleep(3)
	for i in range(thread_num):
		consumer = WeiboConsumer('Weibo_consumer_' + str(i+1), queue)
		consumer.start()
	
