- 充分复用开源项目
- 如何减少测试用例的维护工作  
  -   约定大于配置
  -   在框架中融入最佳自动化实践
  -   测试用例分层  
- pydantic 校验 
- 测试框架基本能力
  -   项目管理：pip、virtualenv  
  -   用例编写：pytest  
  -   领域能力：app、web、http
  -   执行调度：pytest、pycharm、shell、jenkins
  -   测试报告：allure2
  
- http接口测试能力  
  -   请求方法构造：get、post、put、delete、head  
  -   请求体构造：form、json、xml、binary  
  -   响应结果分析：status code、response body 、json path、xpath
  
- hamcrest断言体系  
   -   支持pytest
  
- schema自动校验  
   - 每次运行的时候自动保存当前的schema  
  - 下次运行对比上次的schema，如果发现变更就报错  
  - saveschema+diffschema  
  
- http basic  
  -   基本认证（basic access authentication）：允许http用户代理在请求时，提供用户和密码的一种方式![img.png](img.png)
  -   在自动化中使用auth传递认证参数