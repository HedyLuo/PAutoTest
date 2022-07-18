#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: hedy
@Date: 2022/07/18/23:21 
@Description: 
"""
import requests
from requests.auth import HTTPBasicAuth


class TestAuth:
    # 出现ssl错误，原因是该网站的CA证书未有官方认证
    def test_auth(self):
        r = requests.get('https://httpbin.testing-studio.com/basic-auth/hedy/123',
                         auth=HTTPBasicAuth('hedy', '123'), verify=False)
        print(r.text)

