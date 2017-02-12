CREATE TABLE `position_info` (
  `stock_id` varchar(16) NOT NULL,
  `log_time` datetime NOT NULL,
  `name` varchar(36) NOT NULL DEFAULT '0',
  `price` float NOT NULL DEFAULT '0',
  `count` int(10) unsigned NOT NULL DEFAULT '0',
  `profit` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`log_id`),
  KEY `idx_stock_id` (`stock_id`),
  KEY `idx_log_time` (`log_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8