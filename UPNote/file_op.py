#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: hedy
@Date: 2022/11/08/20:17 
@Description: 文件的内置函数 常用操作：open() write() read() readline() close() seek()
"""

# # 写入文件
# file = open("name.txt", 'w')
# file.write("诸葛亮")
# file.close()
#
# file3 = open('name.txt','a')
# file3.write('刘备')
# file3.close()

# # 读取整个文件
# file1 = open('name.txt')
# print(file1.read())
# file1.close()
#
# # 读取一行
# file2 = open('name.txt')
# # print(file2.readline())
# for line in file2.readlines():
#     print(line)

# 读取指针
file6 = open('name.txt')
print("当前文件指针的位置： %s" %file6.tell())
file6.read(1)
# 第一个参数offset表示偏移位置，第二个参数 0从文件开头偏移 1从当前位置偏移 2从文件结尾
file6.seek(5, 0)
print(file6.tell())
