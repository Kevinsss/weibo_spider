/*
SQLyog v10.2 
MySQL - 5.5.19 : Database - weibo_rss
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`weibo_rss` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `weibo_rss`;

/*Table structure for table `weibo_content` */

CREATE TABLE `weibo_content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `weibo_userid` varchar(50) DEFAULT NULL,
  `weibo_username` varchar(20) DEFAULT NULL,
  `content` text,
  `content_id` varchar(35) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=256 DEFAULT CHARSET=utf8;

/*Table structure for table `weibo_user` */

CREATE TABLE `weibo_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `weibo_userid` varchar(50) DEFAULT NULL,
  `weibo_username` varchar(20) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
