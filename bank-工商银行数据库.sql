/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 8.0.11 : Database - bank
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bank` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `bank`;

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `account` varchar(50) DEFAULT NULL,
  `username` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password` int(11) DEFAULT NULL,
  `country` varchar(10) DEFAULT NULL,
  `province` varchar(10) DEFAULT NULL,
  `street` varchar(10) DEFAULT NULL,
  `door` varchar(10) DEFAULT NULL,
  `money` decimal(18,2) DEFAULT NULL,
  `registerDate` datetime DEFAULT NULL,
  `bankname` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `user` */

insert  into `user`(`account`,`username`,`password`,`country`,`province`,`street`,`door`,`money`,`registerDate`,`bankname`) values ('xEWIfqyY','1',2,'3','4','5','6','1920.00','2021-10-28 16:07:05','中国工商银行昌平支行'),('e0jPCP6r','jason',123456,'cn','cn','cn','cn','2910.00','2021-10-06 17:58:45','中国工商银行昌平支行'),('95nJZAKq','泽塔奥特曼',78,'M78','光之国','露露耶','永恒核心','3000.00','2021-10-29 02:03:09','中国工商银行昌平支行');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
