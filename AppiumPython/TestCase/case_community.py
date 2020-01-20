# -*- coding:utf-8 -*-
# Author：测试小谢
# @FILE     : case_community.py
# @Time     : 2019/12/17 14:08

import unittest
from Page.Community_page import Community
import time
from common.logger import Log
from config.utils import func_time

class Casecommunity(Community, unittest.TestCase):
    log = Log()

    def test_search_success(self):
        '''导航栏切换'''
        try:
            start_process = time.process_time()
            self.switch_navigation()
            end_process = time.process_time()
            # print(end_process - start_process)
            self.log.info("导航栏切换通过,Response time is {}".format(end_process - start_process))

            start_process1 = time.process_time()
            self.search_tap()
            end_process1 = time.process_time()
            self.log.info("跳转搜索切换通过,Response time is {}".format(end_process1 - start_process1))

            self.search_user()
            success1 = self.search_user_success()
            self.assertEqual(success1, '丹姐',msg="搜索功能成功")          #msg相当于备注，断言的话想将msg这句话打印出来
            self.log.info('搜索用户功能正常')

            self.search_dynamic()
            success2 = self.search_dyn_success()
            self.assertEqual(success2, '动态详情展示问题', msg="搜索功能成功")          #搜索动态功能
            self.log.info('搜索动态功能正常')

            # self.search_Vlog()                                                #界面设计获取方式需要改进一下
            # success3 = self.search_dyn_success()
            # self.assertEqual(success3, '武汉的温度居然降了', msg="搜索功能成功")  # 搜索动态功能
            # self.log.info('搜索动态功能正常')

            self.search_cancel()                            #取消搜索的文字
            start_process2 = time.process_time()
            self.search_drop()                              #退出搜索
            end_process2 = time.process_time()
            self.log.info('退出搜索,Response time is {}'.format(end_process2 - start_process2))

            '''           程序部分响应时间
            start_process = time.process_time()
             *********程序                          
            end_process = time.process_time()
            print(end_process - start_process)
            '''

        except Exception as f:              #假如上述操作没有成功，即截图报error
            self.getScreenShot()
            self.log.error(f)




if __name__ == '__main__':
    unittest.main()