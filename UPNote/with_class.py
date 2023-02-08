#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: hedy
@Date: 2023/02/08/22:29 
@Description: 自定义with语句; 异常与类的结合
"""

class Testwith():
    def __enter__(self):
        print("run")
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb is None:
            print("正常结束")
        else:
            print("has error %s" %exc_tb)


with Testwith():
    print("Test is running")
    raise NameError("testNameError")

