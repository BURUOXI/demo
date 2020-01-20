# -*- coding:utf-8 -*-
# Author：测试小谢
# @FILE     : case_peopleNearby.py
# @Time     : 2020/1/8 15:42


import unittest
import traceback
from Page.nearbyPeoplePage import Nearbypeople
from Page.sharePage import Share

from common.logger import Log



class Nearby(Nearbypeople, Share):
    log = Log()

    def nearby_test_success(self):
        try:
            self.nearby_item()
            self.chat_near_item()
            self.tap_friendhost_item()  #跳转到主页
            self.judging_attention_item()
            self.apply_friend_item()
            self.browse_information()
            self.browse_dynamic()

        except Exception as f:  # 假如上述操作没有成功，即截图报error
            self.getScreenShot()
            self.log.error(f)
            traceback.print_exc()




if __name__ == '__main__':
    unittest.main()
