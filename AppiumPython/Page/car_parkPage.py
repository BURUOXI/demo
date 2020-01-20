# -*- coding:utf-8 -*-
# Author：测试小谢
# @FILE     : car_parkPage.py
# @Time     : 2020/1/6 14:28


from Page.BasePage import Action


class Carpack(Action):
    ''' 停车场的页面坐标点 '''
    # 主页面(首页按键)
    Home_Mine= ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[2]/android.widget.RelativeLayout[2]')
    # 停车场
    Home_pack = ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ScrollView/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[1]')
    # 地图无法进行自动化测试，跳过地图进行列表自动化测试
    # 列表跳转
    jump_list = ("id", "com.yzw.yunzhuang:id/iv_menu")
    # 搜索框
    search = ("id", "com.yzw.yunzhuang:id/ll_searchPark")
    #进入搜索界面
    search_button=("id","com.yzw.yunzhuang:id/et_content")
    # 搜索地点，取第一个停车场>>>>判定停车场搜索功能正常
    # 第一个停车场的名字
    first_search_name=("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView[1]")
    # 第一个停车场的地址
    first_search_address=("xpath","/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView[2]")
    # 取消搜索
    cancel_search=("id", "com.yzw.yunzhuang:id/st_cancel")




    # 根据定位，取第一个停车场>>>>>判定停车场定位正常
    first_pack = ("xpath", "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup")
    # 停车场详情>>>>>>>>取停车场title
    pack_detail = ("id", "com.yzw.yunzhuang:id/st_title")

    # com.yzw.yunzhuang: id / et_content

    # 进行入停车场
    def car_pack(self):
        self.click_button(self.Home_Mine)
        self.click_button(self.Home_pack)
        self.click_button(self.jump_list)

    # 列表搜索
    def search_pack(self):
        self.click_button(self.search)
        self.send_keys(self.search_button,"东合中心")
        a = self.find_element(self.first_search_name).text
        b = self.find_element(self.first_search_address).text
        self.click_button(self.cancel_search)

        return a, b

    def normal_list(self):
        self.click_button(self.first_pack)
        a = self.find_element(self.pack_detail).text
        return a
















