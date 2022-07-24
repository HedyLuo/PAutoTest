#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: hedy
@Date: 2022/07/24/16:55 
@Description:
"""
from time import sleep

import allure
import options
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from h5uiauto.pom.fr_pages import CONST_FR as f
from h5uiauto.pom import ChromeSetting, LoginPage, ParaPage

# 填报界面 confirm弹窗第二行内容
from h5uiauto.pom.photoCompare import ImageCompare

em4 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div[1]/div/div/div[2]')
# 填报界面 confirm弹窗第一行内容
em = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div[1]/div/div/div[1]')

# 表单界面，confirm弹窗第二行内容
body_em0 = (By.XPATH, '//*[@id="app"]/div/div[2]/div/div/div/div[1]/div/div/div[2]')
user_name = ['h51', 'h52', 'h53']


@allure.feature("框架冒烟测试")
class TestFrame(object):

    def setup_method(self):
        cs = ChromeSetting()
        self.options = cs.set_chrome(options=options)
        self.driver = webdriver.Chrome(options=self.options)

    def teardown_method(self):
        self.driver.quit()

    @allure.testcase(''.join([f.url_mtt, '4391']))
    @pytest.mark.parametrize('user', user_name)
    def test_mtt4391(self, user):
        lp = LoginPage(self.driver)
        pb = ParaPage(self.driver)
        lp.go_to_url(f.fr_url)
        lp.login(user, f.password)
        sleep(2)
        moban = By.XPATH, "//*[text()='Msg']"
        assert pb.find_element(*moban)
        pb.click_js(*moban)
        sleep(1)

    @allure.testcase(''.join([f.url_mtt, '4330']))
    @allure.testcase(''.join([f.url_mtt, '4622']))
    @allure.description('截图对比目录页的九宫格样式')
    def test_mtt4330_4662(self):
        lp = LoginPage(self.driver)
        pb = ParaPage(self.driver)
        lp.go_to_url(f.fr_url)
        lp.login(f.password, f.password)
        sleep(5)
        pb.get_photo_as_file("../../picture/pic_compare/test1.png")
        sleep(2)
        pc = ImageCompare()
        com = pc.calc_similar_by_path('../../picture/pic_compare/test1.png', '../../picture/pic_correct/test.png')*100
        print('图片对比相似度' + str(com) + "%")
        assert com > 97, '九宫格目录样式失效！'

    @allure.testcase(''.join([f.url_mtt, '5557']))
    def test_mtt5557(self):
        lp = LoginPage(self.driver)
        pb = ParaPage(self.driver)
        lp.go_to_url(f.fr_url)
        lp.login('123', f.password)
        sleep(1)
        assert lp.find_element(By.XPATH, "//*[text()='用户名和密码不匹配']")
        pb.confirm_button()