# -*- coding:utf-8 -*-
# Author：测试小谢
import time

from Page.BasePage import Action


class Community(Action):
    '''首页入口'''
    #首页入口
    home_pa=('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.ImageView')
    #发现
    community_find=('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.TextView')
    # 关注
    community_atten = ('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.TextView')
    # vlog
    community_vlog = ('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[3]/android.widget.TextView')
    # 附近
    community_nearby = ('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[4]/android.widget.TextView')
    # 求助
    community_help = ('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.RelativeLayout[5]/android.widget.TextView')
    #  搜索
    community_search = ('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView')
    #   搜索界面搜索框
    search_frame=('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.EditText')
    #  搜索动态
    search_dyn= ('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[2]/android.widget.TextView')
    #   搜索到第一条动态
    first_dyn=('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]')
    #  搜索用户
    search_member = ('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[2]/android.widget.FrameLayout[1]/android.widget.TextView')
    #       搜索到用户第一条
    first_member=('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[1]')
    #  搜索vlog
    search_vlog = ('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.HorizontalScrollView/android.widget.FrameLayout/android.widget.LinearLayout[3]/android.widget.FrameLayout[3]/android.widget.TextView')
    #   搜索后面X,作用是清除搜索文字
    cancel=('id','com.yzw.yunzhuang:id/iv_close')
    #   退出搜索界面
    drop=('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView')




    def switch_navigation(self):
        '''切换导航栏'''

        self.click_button(self.home_pa)             #进入社区模块
        self.click_button(self.community_find)      #切换至发现
        self.click_button(self.community_atten)     #切换关注
        self.click_button(self.community_vlog)      #切换至vlog
        self.click_button(self.community_nearby)    #切换至附近
        self.click_button(self.community_help)      #切换至互助
        self.click_button(self.community_find)      # 回到发现页面

    def search_tap(self):
        self.click_button(self.community_search)    #社区关注上面搜索框

    def search_user(self):                          #默认搜索用户
        self.click_button(self.search_frame)
        self.clear_key(self.search_frame)
        self.send_keys(self.search_frame,"丹姐")    #默认为搜索用户

    def search_dynamic(self):
        self.click_button(self.search_dyn)
        self.clear_key(self.search_frame)
        self.send_keys(self.search_frame, "猫和老鼠 ")  # 搜索动态

    # def search_Vlog(self):                          #搜索vlog
    #     self.click_button(self.search_vlog)
    #     self.send_keys(self.search_frame, "降温")  # 搜索动态

    def search_cancel(self):                        #取消搜索框内的文字
        # self.click_button(self.search_dyn)
        # self.clear_key(self.search_frame)
        self.send_keys(self.search_frame, "猫和老鼠 ")  # 搜索动态
        self.click_button(self.cancel)              #点击取消按钮

    def search_drop(self):
        self.click_button(self.drop)

    def search_user_success(self):
        '''判断搜索用户是否成功'''
        search_user_success = self.find_element(self.first_member).text
        return search_user_success

    def search_dyn_success(self):
        '''判断搜索动态是否成功'''
        search_dyn_success=self.find_element(self.first_dyn).text
        return search_dyn_success
