#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: hedy
@Date: 2022/11/09/00:31 
@Description: 日期与时间函数库
"""

import time
import datetime as d

print(time.time())
print(time.localtime())
print(time.strftime('%Y-%m-%d %H-%M-%S'))


print(d.datetime.now())
newtime = d.timedelta(minutes=10)
print(d.datetime.now()+newtime)  # 此时的10分钟后

one_day = d.datetime(2022, 11, 9)
new_day = d.timedelta(days=10)
print(one_day+new_day)
