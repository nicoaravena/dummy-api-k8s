CREATE DATABASE IF NOT EXISTS `dummy_instance`;

USE `dummy_instance`;

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
    `id` int(11) UNSIGNED NOT NULL AUTO_INCREMENT,
    `email` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARSET = utf8;

INSERT INTO
    `user` (`email`)
VALUES
    ('user.01@example.org'),
    ('user.02@example.org');
