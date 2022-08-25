
CREATE DATABASE IF NOT EXISTS `db_comeitpack` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `db_comeitpack`;

CREATE TABLE IF NOT EXISTS `clients` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`name` varchar(250) NOT NULL,
	`email` varchar(100) NOT NULL,
    `phone_number` varchar(200) NOT NULL,
	`address_deliv` varchar(255) NOT NULL,
  	`city` varchar(50) NOT NULL,
	`pays` varchar(50) NOT NULL,
	`communication` varchar(50) NOT NULL,
	`brand_id` int(11) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `brand` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`brand_name` varchar(250) NOT NULL,
	`files` varchar(250) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
6