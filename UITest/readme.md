### pytest命令执行
执行文件生成默认路径结果：
pytest test_case01.py -s -q --alluredir=./result  
生成报告：allure serve ./result  

### 其他命令  
设置超时时间：pip3 install --default-timeout=6000 pyyaml