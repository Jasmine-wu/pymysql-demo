### postman

- get请求
    - get请求添加的参数会拼接在url后面
    
- post请求
    - form表单添加添加参数可以上传文件

- Newman输出测试报告支持的格式：

　- -r html,json,junit         指定生成html，json，xml形式的测试报告
　- --reporter-json-export jsonReport.json          生成json格式的测试报告
　- --reporter-junit-export xmlReport.xml            生成xml格式的测试报告
　- --reporter-html-export htmlReport.html          生成html格式的测试报告

- 前提：
    - npm install -g newman-reporter-html 
    - npm install -g newman-reporter-htmlextra

安装地址： /usr/local/lib/node_modules/

- 生成测试报告：

    - newman run HR.postman_collection.json -e 测试环境.postman_environment.json -r html --reporter-html-export report.html
   ：
    - newman run HR.postman_collection.json -e 测试环境.postman_environment.json -r htmlextra --reporter-html-export report.html
    
###  常用接口协议
### 抓包分析TCP协议
    - 三次握手，四次挥手
### curl命令+jq
    - brew install jq
    - jq jason处理
    - curl+jq可以完成多数浏览器能完成的事情

### 常用代理工具
    - charles

