# -*- coding:utf-8 -*-
# Author：测试小谢
# @FILE     : case_pubulish.py
# @Time     : 2020/1/13 17:34


import unittest
from Page.publishPage import Publish
import time
from common.logger import Log
from config.utils import func_time

class CaseLogout(Publish,unittest.TestCase):
    log = Log()

    def test_pubulish_success(self):
        try:
            self.post_news_item()
            self.swipeLeft(500)  # 动态>文章
            self.swipeLeft(500)  # 文章>提问
            # self.post_question_item()



        except Exception as e:
            self.getScreenShot()
            self.log.error(e)


if __name__ == '__main__':
    unittest.main()