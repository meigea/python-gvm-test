MONGO_CONFIG = dict(
    host='192.168.2.73',
    port=27017,
    db_name='openvas_scan',
    username=None,
    password=None
)

import pymysql
MPP_CONFIG = {
    'host': '192.168.2.101',
    'port': 3306,
    'user': 'admin007',
    'password': 'myadmin@816',
    'db': 'ovscan',
    'charset': 'utf8',
    'cursorclass': pymysql.cursors.DictCursor,
}


DBLOG_NAME = "scan_log"
DBLIB_NAME = "scan_lib"


THERATE_CODE = dict(
    High=3,
    Medium=2,
    Low=1,
    Log=0,
)