# -*- coding:utf-8 -*-
# Author：测试小谢
# @FILE     : cmdb.py
# @Time     : 2020/1/13 9:41


#!/usr/bin/python
# -*- coding: UTF-8 -*-

import pymysql
import sys

# 打开数据库连接
db = pymysql.connect("localhost", "root", "123456", "qaq-test", charset='utf8' )
print("登录数据库成功！")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()































