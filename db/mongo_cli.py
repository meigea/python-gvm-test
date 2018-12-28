import pymongo
import sys

from configs.cfg import MONGO_CONFIG
DEFAULT_CONFIG = MONGO_CONFIG

class MongoConn(object):
    def __init__(self, MONGODB_CONFIG=DEFAULT_CONFIG):
        """
        连接配置加载
        :param MONGODB_CONFIG:
        """
        self.MONGODB_CONFIG = MONGODB_CONFIG
        try:
            self.conn = pymongo.MongoClient(self.MONGODB_CONFIG['host'], self.MONGODB_CONFIG['port'])
            self.db = self.conn[self.MONGODB_CONFIG['db_name']]  # connect db
            self.username=self.MONGODB_CONFIG['username']
            self.password=self.MONGODB_CONFIG['password']
            if self.username and self.password:
                self.connected = self.db.authenticate(self.username, self.password)
            else:
                self.connected = True
        except Exception as e:
            print(e)
            sys.exit(1)

    def show_data(self, table='nginx_access_log'):
        """
        答应数据
        :param table:
        :return:
        """
        my_conn = MongoConn()
        res = my_conn.db[table].find(projection={"_id":False})
        for x in res:
            print(x)

    def insert_data(self, table, data):
        """
        插入数据并审计操作
        :param table: 选择集合
        :param data: 选择数据集 列表
        :return:
        """
        from datetime import datetime
        syslog_stat = {"pre_data_len": len(data),
                       "opt_table": table,
                       "stat": "NoneExcept",
                       "runtime": str(datetime.now())}
        try:
            self.db[table].insert(data)
        except:
            pass
        finally:
            self.db["actionlog"].insert(syslog_stat)

    def insert_data_uniq(self, table, data, key="audit_logid"):
        """
        ## 无重插入
        :param table:
        :param data:
        :param key:
        :return:
        """
        # import numpy as np
        try:
            mongo_saved_data = [data[key] for data in self.db[table].find({})]
        except:
            mongo_saved_data = []
        res_data = [item for item in data if item[key] not in mongo_saved_data]

        from datetime import datetime
        syslog_stat = {"pre_data_len": len(data), "opt_table": table, "stat": "Insert【" + str(len(res_data)) + "】条数据", "runtime": str(datetime.now())}
        try:
            self.db[table].insert(res_data)
        except:
            pass
        finally:
            self.db["actionlog"].insert(syslog_stat)

    def show_actions_logs(self):
        """
        审计操作查看
        :return:
        """
        # return self.db["actionlog"].find()
        for x in self.db["actionlog"].find():
            print(x)

    def remove(self, table):
        self.db[table].remove()

    def show_by_condition(self, table, condition={}):
        """
        # 根据条件进行查询，返回所有记录
        :param table:
        :param condition:
        :return:
        """
        res = self.db[table].find(condition)
        for x in res:
            print(x)
