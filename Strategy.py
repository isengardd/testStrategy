#encoding=utf-8
__author__ = 'yao xu'

import easyquotation
import time
import datetime
import StockPool

class Strategy:
    def __init__(self):
        self.m_stocks = StockPool.StockPool()

    def run(self):
        while True:
            if self.is_trade_time():
                self.exec_strategy()

            time.sleep(1)

    def is_trade_time(self):
        nowTime = datetime.datetime.now()
        if nowTime.isoweekday() >= 6:
            return False

        beginTimeAm = datetime.datetime(nowTime.year, nowTime.month, nowTime.day, 9, 30)
        endTimeAm = datetime.datetime(nowTime.year, nowTime.month, nowTime.day, 11,29,45)
        begeinTimePm = datetime.datetime(nowTime.year, nowTime.month, nowTime.day, 13)
        endTimePm = datetime.datetime(nowTime.year, nowTime.month, nowTime.day, 14,29,45)
        if nowTime < beginTimeAm or \
            (nowTime > endTimeAm and nowTime < begeinTimePm) or \
            nowTime > endTimePm:
            return False

        return True

    def exec_strategy(self):
        # 加载远端数据
        self.load_stock_pool()
        # 读取账户资金信息，包括现金和仓位
        #获取每只股票的当前价格
        #决定是否交易

        #从委托列表中执行相应的命令


    def load_stock_pool(self):
        self.m_stocksk.load_stock_pool()



