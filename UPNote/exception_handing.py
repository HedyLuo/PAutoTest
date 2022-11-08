#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: hedy
@Date: 2022/11/09/00:04 
@Description: 异常的检测和处理
"""
try:
    year = int(input("输入年份"))
except ValueError:
    print("年份要输入数字")

# except (ValueError,AttributeError,KeyError)

try:
    print(1/0)
except ZeroDivisionError as e:
    print('o不能作为除数 %s' % e)

# 所有异常类型
# except Exception as e:

try:
    raise NameError('helloerror')
except NameError:
    print("自定义错误类型")


# try finally句式
try:
    a = open('name.txt')
except Exception as e:
    print(e)
finally:
    a.close()