# -*- coding:utf-8 -*-
# @Time   : 2018-11-01 19:24
# @Author : YangWeiMin

from Page.BasePage import Action
import time

from config.utils import func_time


class Login(Action):
    '''登录页面'''
    # 欢迎界面
    welcome_loc = ('id', 'com.yzw.yunzhuang:id/st_passwordLogin')
    # 用户名
    username_loc = ('id', 'com.yzw.yunzhuang:id/et_inputPhone')
    # 密码
    pwd_loc = ('id', 'com.yzw.yunzhuang:id/et_inputCode')
    # 登录
    login_button_loc = ('id', 'com.yzw.yunzhuang:id/st_login')
    # 登录成功后的菜单首页
    login_success_loc = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.ImageView')

    def welcom_user(self):
        '''欢迎界面'''
        self.click_button(self.welcome_loc)

    # def input_errorname(self):
    #     '''输入错误用户名'''
    #     self.send_keys(self.username_loc, '133852896000')
    #     self.send_keys(self.pwd_loc, '666666')
    #     self.click_button(self.login_button_loc)

    def input_username(self):
        '''输入用户名'''
        self.click_button(self.username_loc)
        self.clear_key(self.username_loc)
        self.send_keys(self.username_loc,'13385289600')



    def input_pwd(self):
        '''输入密码'''
        self.click_button(self.pwd_loc)
        self.clear_key(self.pwd_loc)
        self.send_keys(self.pwd_loc,'666666')

    def click_login(self):
        '''点击登录按钮'''
        self.click_button(self.login_button_loc)


    def login_success(self):
        '''判断登录是否成功'''
        # login_success = self.driver.find_element_by_id('com.alipay.android.phone.discovery.o2ohome:id/tab_description').text
        login_success = self.find_element(self.login_success_loc).text
        return login_success


