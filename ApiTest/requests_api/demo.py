#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: hedy
@Date: 2022/07/11/23:46
@Description:
"""
import requests
from jsonpath import jsonpath
from hamcrest import *

payload = {
        "level": 1,
        "name": "hedy"
    }


class TestDemo:
    def test_demo(self):
        r = requests.get('https://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    # get请求
    def test_query(self):
        r = requests.get('https://httpbin.testing-studio.com/get', params=payload)
        print(r.json())
        print(r.text)
        assert r.status_code == 200

    # post请求
    def test_post_form(self):
        r = requests.post('https://httpbin.testing-studio.com/post', data=payload)
        print(r.text)
        assert r.status_code == 200



    # 发送json格式请求
    def test_post_json(self):
        r = requests.post('https://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level'] == 1

    # 接口字段json断言headers
    def test_assert_header(self):
        r = requests.get('https://httpbin.testing-studio.com/get', headers={"h": "header demo"})
        print(r.json())
        assert r.json()['headers']['H'] == 'header demo'

    # 接口字段json断言
    def test_assert_json(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        print(r.text)
        assert r.json()['category_list']['categories'][0]['name'] == '提问区'
        # jsonpath断言
        print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[0] == '提问区'

    # 使用hamcrest断言，github地址:https://github.com/hamcrest/pyhamcrest
    def test_hamcrest(self):
        r = requests.get('https://home.testing-studio.com/categories.json')
        assert_that(r.json()['category_list']['categories'][0]['name'], equal_to('提问区'))

    # 处理header/cookie请求参数
    def test_header(self):
        url = 'https://httpbin.testing-studio.com/cookies'
        header = {
            "User-Agent": 'hedy'
        }
        cookie_data = {
            "name": "hedy",
            'teacher': 'lily'
        }
        r = requests.get(url=url, headers=header, cookies=cookie_data)
        print(r.request.headers)



