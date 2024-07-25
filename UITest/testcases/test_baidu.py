#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: hedy
@Date: 2024/07/25/14:39 
@Description: 
"""
from time import sleep

from selenium import webdriver

def test_baidu():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.baidu.com")
    sleep(10)

