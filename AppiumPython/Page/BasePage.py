# -*- coding:utf-8 -*-
# @Time   : 2018-11-01 19:24
# @Author : YangWeiMin

import unittest

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

from common.logger import Log
from common.read_caps import read_caps
import os





cur_path = os.path.dirname(os.path.realpath(__file__))
screenshot_path = os.path.join(os.path.dirname(cur_path),'screenshots')
if not os.path.exists(screenshot_path):os.mkdir(screenshot_path)

class Action(unittest.TestCase):
    """Base封装公用的方法"""
    def setUp(self):
        print('------开始执行用例------')

    def tearDown(self):
        print('------用例测试结束------')

    @classmethod
    def setUpClass(cls):
        data = read_caps()
        desired_caps = {}

        desired_caps['platformName'] = data['platformName']
        desired_caps['platformVersion'] = data['platformVersion']
        desired_caps['deviceName'] = data['deviceName']
        desired_caps['appPackage'] = data['appPackage']
        desired_caps['appActivity'] = data['appActivity']
        desired_caps['noSign'] = data['noSign']
        desired_caps['noReset'] = data['noReset']
        cls.driver = webdriver.Remote('http://' + data['ip'] + ':' + str(data['port']) + '/wd/hub',desired_caps)
        return cls.driver

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()


    def find_element(self, loc):
        # 重写查找元素方法
        try:
            WebDriverWait(self.driver, 15).until(lambda driver:driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except:
            print('%s 页面中未能找到%s 元素'%(self, loc))


    def clear_key(self,loc):
        """重写清空文本输入法"""
        time.sleep(3)
        self.find_element(loc).clear()


    def send_keys(self, loc, value):
        """重写在文本框中输入内容的方法"""
        self.clear_key(loc) # 先调用
        self.find_element(loc).send_keys(value)


    def click_button(self, loc):
        """重写点击按钮的方法"""
        self.find_element(loc).click()


    def getScreenShot(self):
        """重写截图方法"""
        self.sh_file = os.path.join(screenshot_path, '%s.png' % time.strftime('%Y_%m_%d'))
        self.driver.get_screenshot_as_file(self.sh_file)


    def get_windows_size(self):
        """获取屏幕大小"""
        driver = self.setUpClass()
        windows_size = driver.get_window_size()
        # print(windows_size)
        return windows_size

    def getSize(self):
        '''获取屏幕的宽高'''
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        return (x, y)

    def swipeLeft(self, t):             #向左滑动
        l = self.getSize()
        x1 = int(l[0] * 0.9)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.1)
        self.driver.swipe(x1, y1, x2, y1, 500)

    def swipeRight(self, t):            # 向右滑动
        l = self.getSize()
        x1 = int(l[0] * 0.25)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        self.driver.swipe(x1, y1, x2, y1, 500)

    def swipeUp(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.8)
        y2 = int(l[1] * 0.4)
        self.driver.swipe(x1, y1, x1, y2, 500)

    def swipeDown(self, t):
        l = self.getSize()
        x1 = int(l[0] * 0.5)
        y1 = int(l[1] * 0.35)
        y2 = int(l[1] * 0.85)
        self.driver.swipe(x1, y1, x1, y2, 500)

    def alert(self):

        self.driver.switch_to.alert.accept()
