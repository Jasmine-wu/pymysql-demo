## appium

-  目前mobile自动化的方法

![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/1.png)

- 自动化工具的选择

![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/2.png)
![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/3.png)
![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/4.png)
![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/5.png)
![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/6.png)
![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/7.png)
![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/8.png)
![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/9.png)
![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/10.png)






    混合应用：原生应用嵌套一些网页，如微信小程序
    appium_destop :可录制脚本
    appium是基于node js开发，npm是node js包管理工具
    appium python client: 用于编写自动化测试脚本

    appium环境配置：


    - 安装node js

    - 安装JDK
        mac 上java安装以后要配置环境变量，检查是否安装好：
        - java -version
        - java 
![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/10.png)

![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/配置java环境变量.png)

    - 安装 Andriod SDK
        - 下载地址：http://tools.android-studio.org/index.php/sdk
        - 更新SDK， 下载完以后，解压有个readme文件，有个sdk命令，运行更新sdk，因为有些组件可能没有，需要更新！
                    更新完成SDK，要把整个文件放到一个不常动的目录下。
        - 配置环境变量， 注意一定要加上$PATH, $PATH里面 默认有一些系统的路径
        - source ~/.bash_profile 
        - 验证： adb
![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/11.png)

![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/更新android sdk.png)

![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/android sdk环境变量.png)


    - 安装 appium server
        方法1 ：安装appium desktop（server+inspector工具）
        - https://github.com/appium/appium-desktop/releases/
        - 小白用appium desktop，以后用npm单独安装appium server，
        - desktop启动appium server，直接点击打开
        方法2：
        - 用npm单独安装appium server: npm install -g appium
        - 命令行启动appium server服务： appium
![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/12.png)


    - 安装 appium python client(根据你选择的语言安装对应的client)
        - pip install appium-python-client
        - 验证：在控制台打开python，import appium
![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/13.png)

    - 安装  appium doctor检测 appium安装环境
        - npm -g install appium-doctor
            - 注意：一定要-g全局安装，不然启动appium-doctor的是会报错appium-doctor命令找不到
            - 非全局安装就要非全局卸载 npm uninstal appium-doctor
            - 全局安装就要全局卸载 npm -g uninstal appium-doctor
        - 控制台启动：appium-doctor
![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/15.png)

![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/appium-doctor.png)

    - 验证测试框架能否跑起来
        - 准备一个安卓模拟器 mumu模拟器


![avatar](/Users/neil/PycharmProjects/pythonTest02/app/appImage/16.png)






