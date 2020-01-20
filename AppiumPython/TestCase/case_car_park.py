# -*- coding:utf-8 -*-
# Author：测试小谢
# @FILE     : case_car_park.py
# @Time     : 2020/1/6 14:28

import unittest
from Page.car_parkPage import Carpack
from Page.sharePage import Share
from common.logger import Log
import time
from config.utils import func_time


class CasePack(Carpack, Share, unittest.TestCase):
    log = Log()

    def test_mineDynamic_success(self):
        '''正常存在我的动态'''
        try:
            self.car_pack()
            self.search_pack()
            self.normal_list()

            self.details_shares()
            # self.share_report()
            self.share_shares_share()
            self.share_call_off()
            print("停车场测试完成")




        except Exception as  e:
            self.getScreenShot()
            self.log.error(e)

if __name__ == '__main__':
    unittest.main()

