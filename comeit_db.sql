
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
	`site_web` varchar(250) ,
	`instagram` varchar(250) ,
	`facebook` varchar(250) ,
	`date_crea` varchar(50),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `produits` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`nom` varchar(250),
    `description` varchar(350),
	`type` varchar(100),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;


CREATE TABLE `produits_fixe_prix` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `produit_id` varchar(100),
  `prix_achat_50` varchar(50),
  `prix_achat_100` varchar(50),
  `prix_achat_250` varchar(50),
  `prix_achat_500` varchar(50),
  `prix_achat_1000` varchar(50),
  `prix_vente_50` varchar(50),
  `prix_vente_100` varchar(50),
  `prix_vente_250` varchar(50),
  `prix_vente_500` varchar(50),
  `prix_vente_1000` varchar(50),
  PRIMARY KEY (`id`)
)ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `devis` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`status` varchar(250),
	`client_id` varchar(100),
    `brand_id` varchar(150),
	`total` varchar(255),
  	`date_crea` varchar(50),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `devis_produits_rel` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
	`devis_id` varchar(100),
	`produit_id` varchar(100),
    `description` varchar(350),
	`qte` varchar(100),
  	`prix_achat` varchar(50),
	`prix_vente` varchar(50),
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;



