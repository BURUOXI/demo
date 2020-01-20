# -*- coding:utf-8 -*-
# Author：测试小谢
# @FILE     : get_toast.py
# @Time     : 2019/12/22 10:45

# 重写获取toast方法
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def is_toast_exist(driver, text, timeout=30, poll_frequency=0.5):
    '''is toast exist, return True or False
    :Agrs:
     - driver - 传driver
     - text   - 页面上看到的文本内容
     - timeout - 最大超时时间，默认30s
     - poll_frequency  - 间隔查询时间，默认0.5s查询一次
    :Usage:
     is_toast_exist(driver, "看到的内容")
    '''
    try:
        toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % text)
        print(toast_loc)
        ele = WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(toast_loc))
        return ele.text
    except:
        return False


'''
封装了toast获取，还未进行调试
'''