# -*- coding:utf-8 -*-
# @Time   : 2018-11-13 14:19
# @Author : YangWeiMin

import unittest
from Page.LogoutPage import Logout
import time
from common.logger import Log
from config.utils import func_time


class CaseLogout(Logout,unittest.TestCase):
    log = Log()
    def test_logout_success(self):
        '''正常退出'''
        try:
            self.click_user()

            self.click_setting()
            # self.logout()
            self.click_logout()
            self.alert()
            self.log.info('退出成功')


        except Exception as e:
            self.getScreenShot()
            self.log.error(e)

    # @func_time
    # def logout(self):
    #     self.click_logout()


if __name__ == '__main__':
    unittest.main()