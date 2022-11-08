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

p = re.compile('ca*t')
print(p.match('caaaaat'))  # 输出<re.Match object; span=(0, 1), match='a'>

