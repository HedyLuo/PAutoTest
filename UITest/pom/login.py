#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: hedy
@Date: 2022/07/24/16:51 
@Description: 
"""
# coding = utf-8
from time import sleep

from selenium.webdriver.common.by import By

from UITest.pom.basePage import BasePage


class LoginPage(BasePage):
    usr_name = (By.CSS_SELECTOR, "input[placeholder='请输入用户名']")
    pass_word = (By.CSS_SELECTOR, "input[placeholder='请输入密码']")
    login_button = (By.XPATH, "//*[contains(text(),'登录')]")
    # url = 'http://192.168.5.93:8888/webroot/decision'

    def __init__(self, driver):
        super().__init__(driver)

    def go_to_url(self, url):
        return self.driver.get(url)

    def login(self, usr_name, password):
        sleep(2)
        self.input_text(usr_name, *self.usr_name)
        self.input_text(password, *self.pass_word)
        # self.clear_and_input(password, *self.pass_word)
        self.click(*self.login_button)
        sleep(1)


# if __name__ == '__main__':
#     cs = ChromeSetting()
#     options = cs.set_chrome(options=options)
#     driver = webdriver.Chrome(options=options)
#     url = 'http://192.168.5.93:8888/webroot/decision'
#     lp = LoginPage(driver)//类的实例化
#     lp.go_to_url(url)

