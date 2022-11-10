#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author: hedy
@Date: 2022/11/10/09:26 
@Description: 文件操作库
"""
import os
from pathlib import Path
"""
linux:
建立文件夹 : mdkir wenjianjia
删除文件夹： rmdir wenjianjia  
删除文件夹及文件夹下的文件：rmdir -rf wenjianjia/a 
"""

print(os.path.abspath('.'))  # 当前文件夹下面的绝对路径 /standard_library
print(os.path.abspath('..'))  # 当前文件夹上一层的绝对路径 /upnote
print(os.path.exists('/users'))  # 根目录是否存在
print(os.path.isdir('/Users'))  # 是否是文件夹
os.path.join('/a', 'b')  # 路径连接

# 当前目录文件夹
p = Path('.')
print(p.resolve())

# 创建目录
# q = Path('/a/b/c')
# p.mkdir(q, parents=True)



