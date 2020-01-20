# -*- coding:utf-8 -*-
# Author：测试小谢
# @FILE     : nearbyPeoplePage.py
# @Time     : 2020/1/8 15:41

from Page.BasePage import Action

class Nearbypeople(Action):
    '''附近的人列表'''
    # 主页切换
    Home_near = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.ImageView")
    # 主页>附近的人
    Home_nearby = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ScrollView/android.view.ViewGroup/android.view.ViewGroup[2]/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[5]/android.widget.LinearLayout/android.widget.ImageView")
    # 聊一聊>>>测试功能正常
    nearby_chat = ("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.TextView[3]")
    # 聊天框
    chat_box = ("id", "com.yzw.yunzhuang:id/et_content")
    # 发送
    chat_send = ("id", "com.yzw.yunzhuang:id/st_send")
    # 回退
    back =("id","com.yzw.yunzhuang:id/iv_back")
    # 加好友
    add_friend=("id","com.yzw.yunzhuang:id/st_rightBtn")

    # 附近人的主页
    nearby_page = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[2]")
    # 用户昵称
    member_nickname=("id","com.yzw.yunzhuang:id/st_userName")
    # 关注（未关注状态和关注状态）
    attention =("id","com.yzw.yunzhuang:id/st_attention")

    # 好友状态(加好友，已申请，聊一聊)
    apply_frends = ("id","com.yzw.yunzhuang:id/st_makeFriends")

    # 获取文章数和动态数量
    # 文章
    others_information = ("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView")
    # 资讯详情
    news_details = ("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView")
    #动态
    others_dynamic = ("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.LinearLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView")
    # 动态详情
    dynamic_detail = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[3]")


















    def nearby_item(self):
        self.click_button(self.Home_near)
        self.click_button(self.Home_nearby)

    def nearbyChat_item(self):              # 获取聊一聊的判断依据
        a = self.find_element(self.nearby_chat).text
        return a

    def chat_near_item(self):
        a = self.nearbyChat_item()
        if a == "聊一聊":
            self.click_button(self.nearby_chat)
            self.click_button(self.chat_box)
            self.send_keys(self.chat_box, "自动化脚本发送，不用回复")
            self.click_button(self.chat_send)
            self.click_button(self.back)
        elif a == "加好友":
            self.click_button(self.nearby_chat)
            self.click_button(self.add_friend)

    def tap_friendhost_item(self):
        self.click_button(self.nearby_page)
        a = self.find_element(self.member_nickname).text
        print(a)
        return a

    def get_attention(self):
        b = self.find_element(self.attention).text
        return b

    def judging_attention_item(self):
        b = self.get_attention()
        if b == "+ 关注":
            self.click_button(self.attention)
        else:
            pass

    def get_frend_status(self):
        c= self.find_element(self.apply_frends).text
        return c

    def apply_friend_item(self):
        c = self.get_frend_status()
        if c == "加好友":
            self.click_button(self.apply_frends)
            self.click_button(self.add_friend)
        elif c == "已申请":
            pass
        else:
            self.click_button(self.apply_frends)
            self.click_button(self.chat_box)
            self.send_keys(self.chat_box, "自动化脚本发送，不用回复")
            self.click_button(self.chat_send)
            self.click_button(self.back)

    def get_infor(self):
        d=self.find_element(self.others_information).text
        d1=d[2:4]
        return d1

    def browse_information(self):
        d1= self.get_infor()
        if d1 == "0":
            pass
        else:
            self.click_button(self.news_details)
            self.click_button(self.back)

    def get_dynamic(self):
        e = self.find_element(self.others_dynamic).text
        e1=e[2:4]
        return e1

    def browse_dynamic(self):
        e1= self.get_infor()
        if e1 == "0":
            pass
        else:
            self.click_button(self.dynamic_detail)
            self.click_button(self.back)