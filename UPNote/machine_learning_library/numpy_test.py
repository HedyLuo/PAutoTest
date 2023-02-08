#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: hedy
@Date: 2023/02/08/22:46 
@Description: 
"""
import numpy as np

# arr1 = np.array([2,3,4])
# # dtype查看数据类型
# print(arr1)
# print(arr1.dtype)
#
# arr2 = np.array([1.2,1.3,1.5])
# print(arr2)
# print(arr2.dtype)
#
# print(arr1+arr2)
#
# # 标量计算
# print(arr2 * 10)
#
# data =[[1, 2, 3], [4, 5, 6]]
# # 转成矩阵
# print(np.array(data))
#
# # np.zeros() 矩阵定义
# # ones() 矩阵全部定为1
# # empty() 三维矩阵

# 数组索引和切片
# 0-9的整数
arr4 = np.arange(10)
# 切片 [5,6,7]
print(arr4[5:8])
# 赋值 [ 0  1  2  3  4 10 10 10  8  9]
arr4[5:8] = 10
print(arr4)

# 不加copy arr4为 [ 0  1  2  3  4 15 15 15  8  9]
arr_slice = arr4[5:8].copy()
arr_slice[:] =15
print(arr_slice)
print(arr4)