# -*- coding:utf-8 -*-
# Author：测试小谢
# @FILE     : case_defind.py
# @Time     : 2019/12/19 16:08

import unittest
import time

from Page.sharePage import Share
from Page.unearthPage import unearth

from common.logger import Log
from config.utils import func_time


class CaseDfind(unearth,Share, unittest.TestCase):
    log = Log()

    def test_defind_success(self):
        for i in range(10):
            try:
                self.dynamic_list()
                # self.swipeDown(0)
                self.log.info("进入动态详情")
                self.dynamic_details_get()

                print(self.dynamic_details_get())

                self.log.info(self.dynamic_details_get())       #获取动态详情的作者、年龄、标题、正文、话题、发布时间
                self.log.info('以上是获取动态详情内容')
                self.swipeUp(500)

                self.dynamic_details_com()                      #评论
                """
                需要判断评论是否存在
                """

                self.dynamic_details_likes()                    #点赞
                self.log.info('点赞成功')

                self.dynamic_details_collects()                 #收藏
                self.log.info('收藏成功')
                self.swipeUp(500)
                self.details_comment()                          #评论点赞

                self.details_filter()                           # 筛选
                self.details_shares()                           #进入分享界面
                self.share_report()                             #举报
                self.share_shares_share()                       #分享
                self.share_call_off()                           #取消分享退出分享界面
                print('动态测试完成')
                self.log.info('动态测试完成')
                break

            except Exception as e:
                self.getScreenShot()
                self.log.error(e)
                pass

            continue




