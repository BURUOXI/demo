# -*- coding:utf-8 -*-
# Author：测试小谢
# @FILE     : case_dynamic.py
# @Time     : 2019/12/30 17:53

from Page.myActivityPage import Dynamic
from common.logger import Log
import unittest
from Page.sharePage import Share


class CaseDynamic(Dynamic, Share, unittest.TestCase):
    log = Log()

    def test_mineDynamic_success(self):
        '''正常存在我的动态'''
        for i in range(3):
            try:
                self.Home_Mine()
                self.log.info(self.get_dyna())
                self.swipeUp(500)  # 下滑
                self.swipeLeft(500)  # 动态>文章
                self.swipeLeft(500)  # 文章>提问
                self.log.info(self.get_question())

                self.question_detail()  # 取问题详情
                self.details_shares()  # 进入分享界面
                self.share_report()  # 举报
                self.share_shares_share()  # 分享
                self.share_call_off()  # 取消分享退出分享界面
                self.log.info('我的动态测试完毕')

            except Exception as e:
                self.getScreenShot()
                self.log.error(e)
                pass
            continue

if __name__ == '__main__':
    unittest.main()