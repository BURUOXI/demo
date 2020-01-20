# -*- coding:utf-8 -*-
# Author：测试小谢
# @FILE     : sharePage.py
# @Time     : 2019/12/27 15:41

from Page.BasePage import Action

class Share(Action):
    '''分享小类聚合'''
    # 右上角分享按钮
    details_share=('id', 'com.yzw.yunzhuang:id/iv_share')
    # 举报
    share_inform= ('id', 'com.yzw.yunzhuang:id/iv_report')
    # 分享
    share_shares = ('id', 'com.yzw.yunzhuang:id/iv_app')
    # 分享列表选取好友
    friend_list= ('xpath',"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]")
    # 分享完退出聊天界面
    back_button= ("id", "com.yzw.yunzhuang:id/iv_back")

    #取消
    share_cancel=('id', 'com.yzw.yunzhuang:id/st_cancel')
    #qq
    #微信
    #微博

    def details_shares(self):
        self.click_button(self.details_share)

    def share_report(self):                             # 举报
        self.click_button(self.share_inform)

    def share_shares_share(self):                             # 分享
        self.click_button(self.share_shares)
        self.click_button(self.friend_list)
        self.click_button(self.back_button)            # 返回列表
        self.click_button(self.back_button)             # 返回

    def share_call_off(self):                               # 取消
        self.click_button(self.share_cancel)