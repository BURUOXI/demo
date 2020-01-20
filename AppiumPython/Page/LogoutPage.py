# -*- coding:utf-8 -*-
# @Time   : 2018-11-01 19:24
# @Author : YangWeiMin

from Page.BasePage import Action

class Logout(Action):
    '''退出页面'''
    # 我的
    user_loc = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout[1]/android.widget.FrameLayout[5]/android.view.ViewGroup/android.widget.ImageView')
    # 设置中心
    setting_loc = ('id', 'com.yzw.yunzhuang:id/iv_set')
    # 退出
    logout_loc = ('id', 'com.yzw.yunzhuang:id/cl_logout')
    # 确认退出
    confirm_loc = ('id', 'com.yzw.yunzhuang:id/tvAlert')

    def click_user(self):
        '''进入个人中心'''
        self.click_button(self.user_loc)

    def click_setting(self):
        '''进入设置页面'''
        self.click_button(self.setting_loc)

    def click_logout(self):
        '''点击退出登录按钮'''
        self.click_button(self.logout_loc)
        self.click_button(self.confirm_loc)

    # def click_confirm_logout(self):
    #     self.click_button(self.confirm_loc)
