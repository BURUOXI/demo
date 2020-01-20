# -*- coding:utf-8 -*-
# Author：测试小谢

import time

from common.logger import log_path
from run_main import log
from common.logger import Log

#添加时间计算
def func_time(func):
    def inner(*args, **kw):
        start_time = time.time()
        func(*args, **kw)
        end_time = time.time()
        #print('函数运行时间为：', end_time - start_time, 's')
        # Log.info(end_time - start_time)          #少一个参数



    return inner
