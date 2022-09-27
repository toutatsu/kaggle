from cgitb import lookup
import logging
import sys

class Logger():
    
    default_format = '-'*50+"""
asctime\t\t:%(asctime)s
pathname\t:%(pathname)s
funcName\t:%(funcName)s 
levelname\t:%(levelname)s 
name\t\t:%(name)s
message\t\t:%(message)s
"""+'-'*50

    
    # #ログの出力
    # logger.debug("デバッグ")

    def __init__(self,logger_name):
        #ロガーの生成
        self.logger = logging.getLogger(logger_name)
        #出力レベルの設定
        self.logger.setLevel(logging.DEBUG)
        #ハンドラの生成
        self.handler = logging.StreamHandler(sys.stdout)
        #ロガーにハンドラを登録
        self.logger.addHandler(self.handler)

        #ハンドラにフォーマッタを登録
        self.handler.setFormatter(logging.Formatter(self.default_format))

        
        self.logger.debug("インスタンス生成")