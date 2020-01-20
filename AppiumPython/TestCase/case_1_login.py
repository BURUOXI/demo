# -*- coding:utf-8 -*-
# @Time   : 2018-11-05 19:48
# @Author : YangWeiMin

import unittest
from Page.LoginPage import Login
import time
from common.logger import Log
from config.utils import func_time


class CaseLogin(Login, unittest.TestCase):
    log = Log()
    # def test_login_fail(self):
    #     '''异常登录'''
    #     self.input_errorname()


    def test_login_success(self):
        '''正常登录'''
        try:
            self.welcom_user()
            time.sleep(1)

            self.input_username()
            self.input_pwd()

            self.logon_demo()
            # self.is_toast_exist("登录成功")
            # self.login_success()

            # self.assertEqual(self.login_success(), '首页')
            self.log.info('登录成功')



        except Exception as e:
            self.getScreenShot()
            self.log.error(e)
            # self.is_toast_exist("登录成功")

    @func_time
    def logon_demo(self):
        self.click_login()           #0.77



if __name__ == '__main__':
    unittest.main()
