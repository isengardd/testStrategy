#encoding=utf-8
__author__ = 'yao xu'

import easyquotation
import time


if __name__ == '__main__':
    while True:
        quotation = easyquotation.use('sina')
        result = quotation.stocks(['601919','600616'])
        print(result)
        time.sleep(1)

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