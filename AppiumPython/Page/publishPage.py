# -*- coding:utf-8 -*-
# Author：测试小谢
# @FILE     : publishPage.py
# @Time     : 2020/1/13 14:36


from Page.BasePage import Action

class Publish(Action):
    '''退出页面'''
    # 主页+号
    Home_pubulic = ("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.ImageButton")
    # 发布资讯
    publish_dynamic = ("id", "com.yzw.yunzhuang:id/iv_releaseDynamic")
    # 标题控件
    dynamic_title = ("id","com.yzw.yunzhuang:id/et_title")
    # 正文
    dynamic_body = ("id","com.yzw.yunzhuang:id/et_content")
    # 添加图片
    photo_join = ("id", "com.yzw.yunzhuang:id/iv_pic")
    # 相册选择
    photo_fill = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.TextView")
    # 选择图片
    photo_choose = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[12]/android.view.View")
    # 确定图片
    photo_confirm = ("id", "com.yzw.yunzhuang:id/button_apply")

    # 添加标签
    add_label = ("id", "com.yzw.yunzhuang:id/cl_selectTag")
    # 选择标签
    choose_label = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[2]")
    #添加定位
    add_position = ("id", "com.yzw.yunzhuang:id/st_location")
    # 选择定位
    choose_position = ("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[9]")
    # 提交
    appraise_commit = ("id", "com.yzw.yunzhuang:id/st_rightBtn")

    '''求助部分'''
    # 主页社区
    Home_community = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.ImageView")
    # 互助页面

    # 求助正文
    question_body = ("id", "com.yzw.yunzhuang:id/et_content")




    def post_news_item(self):
        self.click_button(self.Home_pubulic)
        self.click_button(self.publish_dynamic)
        self.send_keys(self.dynamic_title,'自动化测试脚本')
        self.send_keys(self.dynamic_body, "自动化脚本测试")
        self.click_button(self.photo_join)
        self.click_button(self.photo_fill)
        self.click_button(self.photo_choose)
        self.click_button(self.photo_confirm)
        self.click_button(self.add_label)
        self.click_button(self.choose_label)
        self.click_button(self.add_position)
        self.click_button(self.choose_position)
        self.click_button(self.appraise_commit)

    def post_question_item(self):
        self.click_button(self.Home_community)
        # 加右滑
        # self.click_button()                 # 添加发布按钮
        self.send_keys(self.question_body,"自动化测试发布问题")
        self.click_button(self.photo_join)
        self.click_button(self.photo_fill)
        self.click_button(self.photo_choose)
        self.click_button(self.photo_confirm)























