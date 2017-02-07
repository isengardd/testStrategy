#encoding=utf-8
__author__ = 'yao xu'

import pymysql
import os
import json

class StockData:
    def __init__(self, stock_id, price_high, price_high_after_buy, price_N, price_recent_avg):
        self.id = stock_id
        # 近期高点
        self.price_high = price_high
        # 股票的N值
        self.price_N = price_N
        # 股票近期的平均值
        self.price_recent_avg = price_recent_avg
        # 购买后的最高值
        self.price_high_after_buy = price_high_after_buy
class StockPool:
    def __init__(self):
        self.m_stock_pool = dict()
        self.config_path = os.path.dirname(__file__) + '/trader_config.json'
        with open(self.config_path, encoding='utf-8') as f:
             self.config = json.load(f)

    def load_stock_pool(self):
        #读取配置信息
        conn = pymysql.connect(host=self.config['dbhost'], user=self.config['dbuser'], passwd=self.config['passwd'],
                               db=self.config['dbname'], port=int(self.config['dbport']), charset="utf8")
        cursor=conn.cursor()

        cursor.execute("SELECT stock_id,price_high,price_high_after_buy,price_N,price_recent_avg FROM stock_pool")
        rows = cursor.fetchall()
        for row in rows:
            self.m_stock_pool[row[0]] = StockData(row[0], float(row[1]), float(row[2]), float(row[3]), float(row[4]))
            #print(self.m_stock_pool[row[0]].__dict__ )

        cursor.close()
        conn.close()
        pass