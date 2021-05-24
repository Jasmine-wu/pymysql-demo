
Ba-bat123#yy&2


### Jenkin 
163:myse163email@163.com changsha123
Give: myse163 changsha123#

- Mac+postman+jenkins集成测试常见问题：
    - issue1: Newman command not found:
    - 解决方法：
        - echo $PATH
        - 添加jenkins系统环境变量key ：PATH ，value，控制台echo $PATH输出

Issue2:
newman: could not find "report.html" reporter
ensure that the reporter is installed in the same directory as newman
 please install reporter using npm
newman-reporter-html
解决方法：
npm install -g newman-reporter-html 


Issue3：中文乱码
+ newman run HR.postman_collection.json -e $'\213\225\216\203.postman_environment.json' -r report.html
解决方法：
在’全局属性'添加'环境变量'。
LANG=zh_CN.UTF-8和JAVA_TOOL_OPTIONS=- Dfile.encoding=UTF8 

Issue4:HTML Report 样式不正常:
jenkins 上安装 Groovy 插件，用来执行系统 Groovy 脚本，安装完成后，在增加构建步骤里添加：
Execute system Groovy script
执行脚本：System.setProperty("hudson.model.DirectoryBrowserSupport.CSP", "")




