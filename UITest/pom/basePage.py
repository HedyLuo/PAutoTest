#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: hedy
@Date: 2022/07/24/16:08 
@Description: 
"""
"""
类：BasePage（）
作用：封装基本方法，元素查找
"""
from time import sleep

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    # # 查找class，返回列表
    # def find_elements(self, *loc):
    #     return self.driver.find_elements(*loc)

    # 查找单个元素
    # def find_element(self, *loc):
    #     return self.driver.find_element(*loc)

    def find_element(self, by, loc, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).\
                until(lambda driver: driver.find_element(by, loc))
        except (NoSuchElementException, TimeoutException) as e:
            raise e
        else:
            return element

    def find_elements(self, by, loc, timeout=10):
        try:
            elements = WebDriverWait(self.driver, timeout).\
                until(lambda driver: driver.find_elements(by, loc))
        except (NoSuchElementException, TimeoutException) as e:
            raise e
        else:
            return elements

    # def click(self, by, loc, timeout=30):
    #     try:
    #         element = WebDriverWait(self.driver, timeout).\
    #             until(lambda driver: driver.find_element(by, loc)).click()
    #     except (NoSuchElementException, TimeoutException) as e:
    #         raise e
    #     else:
    #         return element
    # 点击元素
    def click(self, *loc):
        sleep(0.4)
        self.find_element(*loc).click()

    # 点击坐标
    def click_chains(self, x, y):
        return ActionChains(self.driver).move_by_offset(x, y).click().perform()

    # 执行JavaScript脚本点击
    def click_js(self, *loc):
        self.driver.execute_script("arguments[0].click();", self.find_element(*loc))

    def clear_js(self, *loc):
        self.driver.execute_script("arguments[0].value = '';", self.find_element(*loc))

    # 点击元素并输入值
    def input_text(self, text, *loc):
        self.find_element(*loc).send_keys(text)

    # 清空元素
    def clear(self, *loc):
        self.find_element(*loc).clear()

    # 清空元素并输入值
    def clear_and_input(self, text, *loc):
        self.find_element(*loc).clear()
        self.find_element(*loc).send_keys(text)

    # 元素是否显示
    def is_display(self, *loc):
        return self.driver.find_element(*loc).is_displayed()

    # 元素是否存在
    def isElementExist(self, *loc):
        flag = True
        try:
            self.find_element(*loc, timeout=2)
            return flag
        except:
            flag = False
            return flag

    # 移动日期控件的面板值、页面滚动操作
    def drag_mouse(self, em1, em2):
        sleep(1)
        ActionChains(self.driver).click_and_hold(self.find_element(*em1)).release(self.find_element(*em2)).perform()
        sleep(1)

    # 页面定位在某个元素位置，可实现页面翻页滚动
    def drag_focus_ele(self, *target):
        sleep(1)
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(*target))
        sleep(1)

    # 获取网页标题
    def get_title(self):
        return self.driver.title

    # 获取当前url
    def get_url(self):
        return self.driver.current_url

    # 获取元素文本
    def get_text(self, *loc):
        return self.find_element(*loc).text

    # 获取单个css属性
    def get_css(self, css, *loc):
        return self.find_element(*loc).value_of_css_property(css)

    # 刷新页面
    def refresh(self):
        return self.driver.refresh()

    # 退出驱动并关闭
    def quit(self):
        self.driver.quit()

    # 关闭当前窗口
    def close(self):
        self.driver.close()

    # 前进
    def forword(self):
        self.driver.forward()

    # 后退
    def back(self):
        self.driver.back()

    # 隐式等待
    def implicitlyWait(self, seconds):
        self.driver.implicitly_wait(seconds)

    # 强制等待
    @staticmethod
    def sleep(seconds):
        sleep(seconds)

    def get_photo_as_file(self, path):
        self.driver.get_screenshot_as_file(path)

    # # cookie操作
    # # 获取cookie
    # def get_cookie(self):
    #     return self.driver.get_cookie()
    #
    # # 删除指定cookie
    # def delete_cookie(self):
    #     self.driver.delete_cookie()
    #
    # # 删除所有cookie
    # def dele_allCookie(self):
    #     self.driver.delete_all_cookie()
    #
    # # 向cookie添加会话
    # def add_cookie(self, cookie_dict):
    #     self.driver.add_cookie(cookie_dict)


