#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: hedy
@Date: 2022/11/09/00:16 
@Description: 常用标准库-正则表达式库re
"""

"""
1. 正则 re
2.
3.
4.
5.
6.通用操作系统 os logging argparse
7.多线程 threading queue
8.internet 数据处理 base64  json urllib
9.结构化标记处理工具 html、xml
10.开发工具 unitest
11.调试工具 timeit
12. 软件包发布的 venv
13.运行服务的 __main__
"""

import re

# # match\group
p = re.compile(r'(\d+)-(\d+)-(\d+)')
# print(p.match('2019-03-10').groups())  # 输出<re.Match object; span=(0, 1), match='a'>
# print(p.match('2019-03-10').group(1))  # 输出<re.Match object; span=(0, 1), match='a'>
# print(r'/n/n')  # r 不转义

# search 模糊匹配
print(p.search('aa2018-03-10bb'))  # 输出 <re.Match object; span=(2, 12), match='2018-03-10'>

# sub()替换函数
phone = '188-7904-1234 # 这是电话号码'
p2 = re.sub(r'#.*$', '', phone)  # 188-7904-1234
p3 = re.sub(r'\D', '', p2)  # 18879041234
print(p2)
print(p3)

# 匹配多次
p4 = re.findall()