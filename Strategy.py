#encoding=utf-8
__author__ = 'yao xu'

import easyquotation
import easytrader
import time
import datetime
import StockPool
import os

class Strategy:
    def __init__(self):
        self.m_stocks = StockPool.StockPool()
        self.m_quotation = easyquotation.use('sina')
        self.m_trader = easytrader.use('yjb', False)
        config_path = os.path.dirname(__file__) + '/trader_config.json'
        self.m_trader.prepare(config_path)

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
        my_balance = self.m_trader.balance
        print(my_balance)
        my_position = self.m_trader.position
        print(my_position)

        #获取每只股票的当前价格
        for idx in self.m_stocks.m_stock_pool.keys():
            stock_data = self.m_stocks.m_stock_pool[idx]
            print(stock_data.id)
            result = self.m_quotation.stocks(stock_data.id)
            if result is None:
                easytrader.log.info("request %s stock info failed!" %stock_data.id)
            else :
                print(result)
            #决定是否交易
            self.decide_sell()
            self.decide_buy()

        #从委托列表中执行相应的命令


    def load_stock_pool(self):
        self.m_stocks.load_stock_pool()

    def decide_sell(self):
        pass

    def decide_buy(self):
        pass


