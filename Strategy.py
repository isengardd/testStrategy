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
        self.m_trader = easytrader.use('gf', False)
        config_path = os.path.dirname(__file__) + '/trader_config.json'
        self.m_trader.prepare(config_path)
        self.m_balance = None
        self.m_position = None

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
        self.m_balance = self.m_trader.balance
        #print(my_balance)
        self.m_position = self.m_trader.position
        #print(my_position)

        #获取每只股票的当前价格
        for idx in self.m_stocks.m_stock_pool.keys():
            stock_data = self.m_stocks.m_stock_pool[idx]
            print(stock_data.id)
            result = self.m_quotation.stocks(stock_data.id)
            if result is None:
                easytrader.log.info("request %s stock info failed!" %stock_data.id)
                continue
            else :
                #print(result)
                # todo: 解析result ，并更新历史最高价（如果需要的话）
                stock_data.update_price_after_buy(result['now'])

            #决定是否交易
            self.update_entrust()
            self.decide_sell(stock_data, result['now'])
            self.decide_buy(stock_data, result['now'])

        #todo: 从委托列表中执行相应的命令


    def load_stock_pool(self):
        self.m_stocks.load_stock_pool()

    def update_entrust(self):
        # todo: 根据委托状态决定是否撤单

    def decide_sell(self, stock_data, curPrice):
        # 如果未持有股票，直接返回
        if self.is_hold_stock() == False:
            return

        # todo:获取持仓信息
        for stockPos in self.m_position:
            if stockPos['stock_code'] != stock_data.id:
                continue

            if curPrice > stock_data.close*0.900 and \
            not self.is_buy_today() and \
            stock_data.price_high_after_buy != stockPos['cost_price'] and \
            can_sell_out():
                self.sell_stock()

    def decide_buy(self, stock_data, curPrice):
        #如果已持有股票，暂时不考虑追加持有
        if self.is_hold_stock():
            return

        # todo:根据当前价格决定是否购买
        if stock_data.price_high != stock_data.price_high_today and \
            #self.DiffDayLastSellOut(stock.m_stockId, context.current_dt, 10) and
        curPrice * 1.20 >= stock_data.price_high and \
        curPrice < stock_data.close*1.098:
            self.buy_stock()


    def sell_stock(self):
        pass

    def buy_stock(self):
        #todo: 检查是否已委托或者已持仓，然后向券商下单
        pass

    def is_hold_stock(self):
        return False

    def is_buy_today(self):
        #todo: 判断该只股票是否是在今日购买
        return False

    def can_sell_out(self):
        return False