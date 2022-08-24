
CREATE DATABASE IF NOT EXISTS `db_comeitpack` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `db_comeitpack`;

CREATE TABLE IF NOT EXISTS `clients` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`firstname` varchar(50) NOT NULL,
	`lastname` varchar(50) NOT NULL,
	`email` varchar(100) NOT NULL,
    `phone_number` varchar(100) NOT NULL,
	`type_c` varchar(50) NOT NULL,
  	`password` varchar(255) NOT NULL,
	`token` varchar(500) NOT NULL,
	`validation` int(11) NOT NULL DEFAULT 0,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
