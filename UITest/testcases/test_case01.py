#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: hedy
@Date: 2022/07/24/16:55 
@Description:
"""
from time import sleep
import pytest
from selenium import webdriver
import options
from selenium.webdriver.common.by import By

from UITest.pom.basePage import BasePage
from UITest.pom.chrome_setting import ChromeSetting
from UITest.pom.login import LoginPage

card_info = [
    ['a', 'b', 'c', 'e', 'e'],
]


class TestCard(object):

    def setup_method(self):
        cs = ChromeSetting()
        self.options = cs.set_chrome(options=options)
        self.driver = webdriver.Chrome(options=self.options)

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("a,b,c,d,e", card_info)
    def test_cardVersion(self, a, b, c, d, e):
        lp = LoginPage(self.driver)
        lp.go_to_url(b)
        sleep(3)
        bp = BasePage(self.driver)
        card_ele = (c, d)
        card_version = bp.find_element(*card_ele).get_attribute("data-version")
        # card_version = bp.get_attribute_rewrite(*card_id, "data-version")
        print(a+"的卡片版本是："+card_version)
        assert card_version == e
