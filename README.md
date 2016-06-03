# weibo_spider

## Description
	Reading userid list(not nickname) from Weibo_user table in MySQL,then crawl these user's Weibo message and save messages to database(MySQL).
	main.py: start py.
	MysqlUtil.py: connect to MySQL and execute CRUD operations.
	WeiboProducer.py: read userid list from MySQL and put userids in to the queue
	WeiboConsumer.py: read userid from the queue and crawl Weibo message.
	weibo_rss.sql: database sql,include table structure.

## Environment
	Python: 2.7.*
	System: Ubuntu
	MySQL: 5.5

## Usage
To run main.py normaly, you need do these:

1. you need to login [weibo.cn](http://weibo.cn)(Mobile page) to get login cookie.
2. copy cookies, set to variable: cookie in WeiboConsumer.py line 25. 
3. install MySQL and create database,tables.
4. set start parameters: -t (Weiboconsumer thread numbers)(Optional)

Example:

	python main.py -t 3

## How to get cookie:
1. open [weibo.cn](http://weibo.cn) in Firefox or Chrome.
2. open developer tools -> NetWork， find weibo.cn login request header.
3. copy cookie in request header to program.

![image](https://github.com/Kevinsss/weibo_spider/blob/master/result.png)




