#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: hedy
@Date: 2022/07/24/16:55 
@Description:
"""
import time
from time import sleep
import pytest
from selenium import webdriver
import yaml
import options
from selenium.webdriver.common.by import By

from UITest.pom.basePage import BasePage
from UITest.pom.chrome_setting import ChromeSetting
from UITest.pom.login import LoginPage

card_info = [
    ['a', 'https://work.weixin.qq.com/wework_admin/frame', 'c', 'e', 'e'],
]


class TestCard(object):

    def setup_method(self):
        # 使用默认浏览器窗口
        self.driver = webdriver.Chrome()

        # 设置为h5手机模式显示窗口
        # cs = ChromeSetting()
        # self.options = cs.set_chrome(options=options)
        # self.driver = webdriver.Chrome(options=self.options)
    def teardown_method(self):
        self.driver.quit()

    def test_weixin_login(self):
        bp = BasePage(self.driver)
        bp.go_url("https://work.weixin.qq.com/wework_admin/frame")
        sleep(20)
        cookie = bp.get_cookies()
        with open("../ddt/cookie.yaml", 'w') as f:
            yaml.safe_dump(cookie, f)

    def test_weixin01(self):
        bp = BasePage(self.driver)
        bp.go_url("https://work.weixin.qq.com/wework_admin/frame")
        cookie = yaml.safe_load(open("../ddt/cookie.yaml"))
        for c in cookie:
            bp.add_cookie(c)
        sleep(3)
        bp.go_url("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)
        bp.get_photo_plus_path()
        sleep(1)
        tongxunlu = (By.CLASS_NAME,"frame_nav_item_title")
        assert bp.find_elements(*tongxunlu)[1].text == "通讯录"


    # @pytest.mark.parametrize("a,b,c,d,e", card_info)
    # def test_cardVersion(self, a, b, c, d, e):
    #     lp = LoginPage(self.driver)
    #     lp.go_to_url(b)
    #     sleep(3)
    #     bp = BasePage(self.driver)
    #     card_ele = (c, d)
    #     card_version = bp.find_element(*card_ele).get_attribute("data-version")
    #     # card_version = bp.get_attribute_rewrite(*card_id, "data-version")
    #     print(a+"的卡片版本是："+card_version)
    #     assert card_version == e
