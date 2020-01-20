# -*- coding:utf-8 -*-
# Author：测试小谢
# @FILE     : stationPage.py
# @Time     : 2020/1/7 13:49

from Page.BasePage import Action

class Station(Action):

    ''' 充电站的页面坐标点 '''
    # 主页面(首页按键)
    Home_Mine= ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]')
    # 充电站
    Home_station=("id", "com.yzw.yunzhuang:id/st_charge")
    # 地图暂时不做处理，直接做列表
    # 跳转列表
    station_list=("id","com.yzw.yunzhuang:id/iv_menu")
    # 获取列表第一个，判定充电站周围有数据，否则没有数据
    # 获取第一个充电站名字
    list_first_station= ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[1]")
    # 进入详情
    first_station_detail=("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup")
    # 用户评价
    user_evaluation= ("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.TextView")
    # 用户名
    user_name=("id","com.yzw.yunzhuang:id/st_userName")
    # 用户的评价
    users_appraise= ("id","com.yzw.yunzhuang:id/st_evaluation")
    # 评论功能
    back_button= ("id", "com.yzw.yunzhuang:id/iv_back")
    # 电站详情
    station_detail= ("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView")
    # 评论
    evalua_appraise= ("id","com.yzw.yunzhuang:id/cl_estimate")
    # 输入评论
    appraise_words =("id","com.yzw.yunzhuang:id/et_inputComment")
    # 提交
    appraise_commit=("id","com.yzw.yunzhuang:id/st_rightCommit")

    # 纠错
    error_correction =("id","com.yzw.yunzhuang:id/cl_errorRecovery")

    # 信息错误
    message_error=("id","com.yzw.yunzhuang:id/iv_grogshop")
    # 填写信息   和评论一样
    message_fill= ("id","com.yzw.yunzhuang:id/et_inputComment")
    # 添加图片
    photo_fill = ("id","com.yzw.yunzhuang:id/iv_pic")
    # 选择图片
    photo_choose =("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[12]/android.view.View")
    # 确认
    photo_confirm=("id","com.yzw.yunzhuang:id/button_apply")
    # 提交

    # 位置错误
    position_error=("id","com.yzw.yunzhuang:id/st_grogshop")
    # 说明错误
    description_error = ("id","com.yzw.yunzhuang:id/et_inputText")
    # 提交
    submit=("id","com.yzw.yunzhuang:id/st_commit")
    # 收藏
    collect=("id","com.yzw.yunzhuang:id/iv_collect")

    def charging_station (self):
        self.click_button(self.Home_Mine)
        self.click_button(self.Home_station)
        self.click_button(self.station_list)

    def station_item(self):
        a = self.find_element(self.list_first_station)
        print(a)
        self.click_button(self.first_station_detail)
        return a

    def evaluation_item(self):                          #查看评论模块
        self.click_button(self.user_evaluation)
        a = self.find_element(self.user_name)
        b = self.find_element(self.users_appraise)
        print(a,b)
        return a,b

    def appraise_item(self):                            #写评论模块
        self.click_button(self.station_detail)
        self.click_button(self.evalua_appraise)
        self.send_keys(self.appraise_words,'充电站自动化测试')
        self.click_button(self.appraise_commit)

    def error_correction_item(self):
        self.click_button(self.error_correction)
        self.click_button(self.message_error)
        self.send_keys(self.message_fill,"充电站信息纠错自动化测试")
        self.click_button(self.photo_fill)          # 添加图片
        self.click_button(self.photo_choose)
        self.click_button(self.photo_confirm)
        self.click_button(self.appraise_commit)    # 提交

    def error_position_item(self):
        self.click_button(self.error_correction)
        self.click_button(self.position_error)
        self.send_keys(self.description_error,"位置偏离自动化测试")
        self.click_button(self.submit)

    def collect_item(self):
        self.click_button(self.collect)













