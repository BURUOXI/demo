# -*- coding:utf-8 -*-
# Author：测试小谢
# @FILE     : unearthPage.py
# @Time     : 2019/12/18 14:15

from Page.BasePage import Action

class unearth(Action):
    '''发现主界面'''
    # 社区
    community_unearth=('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.ImageView')
    # 第一条点击动态
    community_dyn=('xpath','/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView[1]')
    # 第一条标题()
    community_dyn_title=('id','com.yzw.yunzhuang:id/st_richTitle')
    # 动态详情---获取作者姓名
    defynamic_details_author=('id','com.yzw.yunzhuang:id/st_userName')
    # 动态详情---年龄
    defynamic_details_age=('id','com.yzw.yunzhuang:id/st_userAge')
    # 动态详情---标题
    defynamic_details_title=('id','com.yzw.yunzhuang:id/st_richTitle')
    # 动态详情---正文
    defynamic_details_text=('id','com.yzw.yunzhuang:id/st_content')
    # 动态详情---话题
    defynamic_details_topic = ('id', 'com.yzw.yunzhuang:id/st_tag')
    # 动态详情---发布时间
    defynamic_details_time = ('id', 'com.yzw.yunzhuang:id/st_richDate')
    # 动态详情---评论
    defynamic_details_comment=('id', 'com.yzw.yunzhuang:id/st_writeReview')
    #
    defynamic_details_comment1=('id', 'com.yzw.yunzhuang:id/et_inputComment')
    # 动态详情---评论---提交
    defynamic_details_comment1_send=('id', 'com.yzw.yunzhuang:id/st_send')
    # 动态详情---点赞
    defynamic_details_like=('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView[2]')
    # 动态详情---收藏
    defynamic_details_collect=('id', 'com.yzw.yunzhuang:id/iv_collect')
    # 动态详情---评论--点赞
    details_comment_like=('xpath', '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.view.ViewGroup/android.support.v7.widget.RecyclerView/android.view.ViewGroup/android.widget.ImageView[2]')
    # 动态详情---评论--筛选
    details_comment_filter=('id', 'com.yzw.yunzhuang:id/st_filtrate')
    # 评论热度排行
    details_comment_hot=('id', 'com.yzw.yunzhuang:id/st_hot')
    # 评论时间排行
    details_comment_time = ('id', 'com.yzw.yunzhuang:id/st_time')




    def dynamic_list(self):
        self.click_button(self.community_unearth)
        self.click_button(self.community_dyn)
        dynamic_list_title = self.find_element(self.community_dyn_title).text

        return dynamic_list_title

    def dynamic_details_get(self):              #获取动态的作者、年龄、标题、正文
        a=self.find_element(self.defynamic_details_author).text
        b=self.find_element(self.defynamic_details_age).text
        c= self.find_element(self.defynamic_details_title).text
        d = self.find_element(self.defynamic_details_text).text
        e = self.find_element(self.defynamic_details_topic).text
        f = self.find_element(self.defynamic_details_time).text
        return a,b,c,d,e,f

    def dynamic_details_com(self):
        self.click_button(self.defynamic_details_comment)
        self.send_keys(self.defynamic_details_comment1,'自动化评论测试')
        self.click_button(self.defynamic_details_comment1_send)

    def dynamic_details_likes(self):
        self.click_button(self.defynamic_details_like)

    def dynamic_details_collects(self):
        self.click_button(self.defynamic_details_collect)

    def details_comment(self):
        self.click_button(self.details_comment_like)

    def details_filter(self):                               #筛选
        self.click_button(self.details_comment_filter)
        self.click_button(self.details_comment_hot)
        self.click_button(self.details_comment_filter)#热度排序
        self.click_button(self.details_comment_time)







    # def dynamic_list_title(self):
    #     '''获取动态列表中动态标题'''
    #     dynamic_list_title = self.find_element(self.community_dyn_title).text
    #     return dynamic_list_title

