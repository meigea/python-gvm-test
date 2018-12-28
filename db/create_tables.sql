DROP TABLE IF EXISTS `scanlib`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scanlib` (
  `oid` varchar(255) NOT NULL,
  `oname` varchar(255) NOT NULL,
  `summary` text NOT NULL DEFAULT '',
  `solution` text NOT NULL DEFAULT '',
  `vuldetect` text NOT NULL DEFAULT '',
  `threat_code` int(3) NOT NULL DEFAULT 0,
  `family` varchar(255) NOT NULL DEFAULT '',
  `impact` text NOT NULL DEFAULT '',
  `security` varchar(25) NOT NULL, DEFAULT '0.0',
  `info_type` varchar(255) NOT NULL DEFAULT 'nvt',
  PRIMARY KEY (`oid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS `scanlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scanlog` (
  `id` varchar(255) NOT NULL,
  `report_id` varchar(255) NOT NULL,
  `vulner_desc` text NOT NULL,
  `host` varchar(255) NOT NULL,
  `port` varchar(255) NOT NULL,
  `add_time` varchar(255) NOT NULL,
  `oid` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;


DROP TABLE IF EXISTS `scan_task_temp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `scan_task_temp` (
  `task_id` varchar(255) NOT NULL,
  `t_status` tinyint(3) unsigned DEFAULT '0' COMMENT '任务执行状态：\r\n0： 未执行\r\n1： 执行中\r\n2：执行结束',
  `t_ecode` int(10) unsigned DEFAULT '0' COMMENT '执行结束后。\r\n任务的最终状态码。\r\n0： 执行过程中没有异常错误',
  `t_add_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `t_update_time` timestamp NULL DEFAULT NULL,
  `t_progress` tinyint(10) unsigned DEFAULT '0',
  `has_results` int(10) unsigned DEFAULT '0',
  PRIMARY KEY (`task_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='扫描表:\r\n规定 ips 的格式 仅能为 ip1 , ip2,... 。 方便扫描方便回收。\r\nports 的格式  依旧。\r\n当前此表未 任务表的拷贝，其主要作用是，将数据 触发到 其它表中\r\n\r\ninsert ,update  触发操作更新到其它数据库的任务表';
/*!40101 SET character_set_client = @saved_cs_client */;
