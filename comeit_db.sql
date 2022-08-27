
CREATE DATABASE IF NOT EXISTS `db_comeitpack` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `db_comeitpack`;

CREATE TABLE IF NOT EXISTS `clients` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`name` varchar(250),
	`email` varchar(100),
    `phone_number` varchar(200),
	`address_deliv` varchar(255),
  	`city` varchar(50),
	`pays` varchar(50),
	`communication` varchar(50),
	`brand_id` varchar(150) NOT NULL,
	`date_crea` varchar(50),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `brand` (
	`id` varchar(150) NOT NULL ,
	`brand_name` varchar(250) ,
	`files` varchar(250) ,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
6