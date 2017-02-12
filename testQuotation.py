#encoding=utf-8
__author__ = 'yao xu'

import Strategy


if __name__ == '__main__':
    new_strategy = Strategy.Strategy()
    new_strategy.exec_strategy()

'''def onInterval():
    quotation = easyquotation.use('sina')
    result = quotation.stocks('601919')
    print(result)

    global timer
    timer = threading.Timer(1.0, onInterval, [])
    timer.start()

if __name__ == "__main__":
    timer = threading.Timer(1.0, onInterval, [])
    timer.start()'''