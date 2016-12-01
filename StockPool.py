#encoding=utf-8
__author__ = 'yao xu'

class StockHistory:
    def __init__(self, stock_id, price_high, price_N, price_recent_avg):
        self.id = stock_id
        self.price_high = price_high
        self.price_N = price_N
        self.price_recent_avg = price_recent_avg

class StockPool:
    def __init__(self):
        self.m_stock_pool = dict()

    def load_stock_pool(self):
        #读取配置信息
        pass