# -*- coding:utf-8 -*-
# Author：测试小谢
# @FILE     : myActivityPage.py
# @Time     : 2019/12/30 17:41

from Page.BasePage import Action

class Dynamic(Action):
    '''我的动态页面'''
    #我的（首页面跳转）
    Mine = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.ImageView')
    # 我的动态
    Mine_dyna= ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.view.ViewGroup[1]')
    # 第一篇动态标题、作者
    fir_dyna=("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[3]")
    fir_author=("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[1]")
    #

    #提问内容、作者
    fir_question = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView[4]" )
    fir_author2 = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]")

    # 提问
    question_demo = ("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView[4]")



    def Home_Mine(self):
        self.click_button(self.Mine)  # 首页>我的
        self.click_button(self.Mine_dyna)  # 我的>我的动态

    def get_dyna(self):
        res = self.find_element(self.fir_dyna).text
        res1 = self.find_element(self.fir_author).text
        return res, res1

    def get_question(self):
        res2 = self.find_element(self.fir_question).text
        res3 = self.find_element(self.fir_author2).text
        return res2, res3


    def question_detail(self):
        self.click_button(self.question_demo)

