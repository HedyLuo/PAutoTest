#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: hedy
@Date: 2022/07/24/16:51 
@Description: 
"""
setting_ = """
类：ChromeSetting()
作用：浏览器参数设置
"""
from selenium import webdriver
class ChromeSetting(object):
    def set_chrome(self, options):
        mobileH5 = {'deviceName': 'iPhone X'}
        options = webdriver.ChromeOptions()
        options.add_experimental_option('mobileEmulation', mobileH5)
        options.add_argument("--window-size=240,1600")
        options.add_argument('disable-infobars')
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("excludeSwitches", ['enable-automation'])
        # driver = webdriver.Chrome(options=options)
        # driver.implicitly_wait(30)
        # return driver
        return options
