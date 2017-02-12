CREATE TABLE `stock_pool` (
  `stock_id` varchar(16) NOT NULL,
  `stock_flag` int(10) unsigned NOT NULL DEFAULT '0',
  `price_high` float NOT NULL DEFAULT '0',
  `price_high_after_buy` float NOT NULL DEFAULT '0',
  `price_N` float NOT NULL DEFAULT '0',
  `price_recent_avg` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`stock_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8