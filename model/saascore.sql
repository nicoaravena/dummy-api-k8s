CREATE DATABASE IF NOT EXISTS `dummy_saas_db`;

USE `dummy_saas_db`;

DROP TABLE IF EXISTS `instance_data`;

CREATE TABLE `instance_data` (
    `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `name` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8;

INSERT INTO
    `instance_data` (`name`)
VALUES
    ('foo'),
    ('bar');
