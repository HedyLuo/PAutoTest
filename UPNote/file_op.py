#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: hedy
@Date: 2022/11/08/20:17 
@Description: 
"""

# 写入文件
file = open("name.txt", 'w')
file.write("诸葛亮")
file.close()

# 读取文件
file1 = open('name.txt')
print(file1.read())
file1.close()

file3 = open('name.txt','a')
file3.write('刘备')
file3.close()
