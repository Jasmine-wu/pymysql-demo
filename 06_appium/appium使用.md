

   ## 连接模拟器
    注意事项
    - 网易mumu针对android6.0进行了改造，是固定版本的。
    - sdk自带的模拟器有各种版本的
    - 用真机需要root权限，要下载一个root adk对真机进行root
    - 对于andorid来说每一个页面都是一个appActivity,测试要指定哪个包哪个页面
    - appPakage name 是唯一标识
    - automationname 引擎名字
    
    连接模拟器

    - 打开mumu模拟器
    - 控制台输入adb devices 查看模拟器是否链接
    - 如果只出现List of devices attached，输入adb version 查看adb版本不是在1.0.3以上，然后adb kill-server，再重新输入adb devices
    - 开启appium服务
    - 在destop上start一个secsstion，只add两个capbilities:"platformName": "android", "deviceName": "emulator-5554",
      不需要传入appPakcage和appActivity，就可以连接到模拟器，然后在模拟器里直接操作

        Android真机调试：
            - 打开调试模式
            设置-》最下面有个关于-〉最下面有个版本号，连点七下，就会处于开发者模式，在返回上一页，会多出来一个开发者选项-》点击开发者选项-〉打开USB调试，打开指针位置
            - 如果android设备连接在windows上还需要安装驱动程序，手机助手，豌豆荚会自动帮我们安装这个驱动程序
        IOS：
        Xcode自带模拟器,但是他需要额外的一些工具包，比如libimobiledevice, ideviceinstaller, WDA(appium做自动化测试的时候需要安装到手机上的包)

        如何安装应用
            - 模拟器可以下载apk包直接把apk包拖进来，真机可以使用手机助手或者豌豆荚。或者命令行安装 
            - adb install 安装包地址
            - adb intall -r 安装包地址 覆盖安装
            - adb unintall 包名 卸载应用
### 运行测试用例
    - 打开mumu模拟器
    - 控制台输入adb devices 查看模拟器是否链接
    - 如果只出现List of devices attached，输入adb version 查看adb版本不是在1.0.3以上，然后adb kill-server，再重新输入adb devices
    - 开启appium服务
    - run testcode
   
    - 常见报错：
        - android sdk build-tools 版本太高，与java版本不匹配

         java.lang.UnsupportedClassVersionError: com/android/apksigner/ApkSignerTool has been compiled by a more recent version of the Java Runtime (class file version 53.0),

        解决：下载低版本android build-tools
            - https://androidsdkmanager.azurewebsites.net/Buildtools
            - 解压修改对应版本号放在 android build tool 目录，如果还报错，删掉30版本的

        -  Could not find a connected Android device in 20227ms.
            - 看模拟器是否打开
            - 查看看模拟器是否连接上
                - adb devices 如果模拟器打开了，但是这里没连接上，输入adb kill-server ,然后再输入adb devices
                    如果显示该设备offline，再输入adb devices，就可以看到该设备了

```commandline
                neil@NeildeMacBook-Pro ~ % adb devices 
                List of devices attached
                
                neil@NeildeMacBook-Pro ~ % adb kill-server
                neil@NeildeMacBook-Pro ~ % adb devices    
                * daemon not running; starting now at tcp:5037
                * daemon started successfully
                List of devices attached
                emulator-5554	offline
                
                neil@NeildeMacBook-Pro ~ % adb devices
                List of devices attached
                emulator-5554	device
                
                neil@NeildeMacBook-Pro ~ % 
```


    
      - 常用capbilities参数：
            - https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md
            - skipDeviceInitialization 这个参数，当执行的测试用例很多的时候可以大提升整体的运行时间
    

     - 常用命令

       - 查看当前activity: 可以用来查看当前activity的名字
            - adb shell dumpsys activity top
       - 查看所有activity
             - adb shell dumpsys activity activities
       - 启动某个activity
            - adb shell am start -W -n com.xueqiu.android/.common.search.USearchActivity

        - 如何获取appPackage和appActivity ？
             - adb logcat | grep -i displayed 
                点击你要打开的app和页面 ，在控制台可以监控到输出：
```commandline
                neil@NeildeMacBook-Pro ~ % adb logcat | grep -i displayed
                03-17 22:27:48.993   669   688 I ActivityManager: Displayed io.appium.settings/.Settings: +2s728ms
                03-17 22:31:31.861   669   688 I ActivityManager: Displayed com.mumu.store/.search.LauncherSearchActivity: +1s134ms
                03-17 22:32:54.692   669   688 I ActivityManager: Displayed com.taobao.taobao/com.taobao.tao.welcome.Welcome: +25s783ms
                        -appPackage ： com.taobao.taobao
                        -appActivity： .search.LauncherSearchActivity
                        
                        
```  
        - 另一种方法：获取窗口当前页，输出更简洁
```commandline
neil@NeildeMacBook-Pro ~ % adb shell dumpsys window | grep mCurrent
    mCurrentAppOrientation=1
      mCurrentRotation=0
        mCurrentUserId=0
  mCurrentFocus=Window{63e02bb u0 com.xueqiu.android/com.xueqiu.android.community.UserProfileActivity}
neil@NeildeMacBook-Pro ~ % 

``` 
        - 获取当前手机chrome版本
```commandline
neil@NeildeMacBook-Pro ~ % adb shell pm list package | grep webview
package:com.android.webview
neil@NeildeMacBook-Pro ~ % adb shell pm dump com.android.webview | grep version
      versionCode=275610060 targetSdk=24
      versionName=52.0.2743.100
neil@NeildeMacBook-Pro ~ % 

```
        appium server：
                监听和转发
                
                Server可以放在本地，也可以放在云端。
                appActivty: 必须重第一个页面进去
                
                实际工作中，要配置一个服务器，专门运行appium server
                启动：
                    appium -a 服务器ip -p 端口号
                打印appium日志
                    appium -g  日志名




### 元素定位

- 通过id定位
- 通过accessibiity id 定位，accessibiity id其实是content-desc属性的值
- appium 是不支持text属性定位的，如果要通过text属性定位，需要用到uiautomator定位


- 定位工具uiautomatorviewer
    - which uiautomatorviewer
    - 如果只做andorid的自动化建议用这个工具
    - 只需点击第二个按钮就会自动加载模拟器的当前页，没有appium那些复杂的capbiliities设置
  
    - 常见报错：
      - error obtaining UI hierarchy：
            - jdk 降级，切换成低版本的，1.8.211这个版本可用28的不可用
        
     - Error while obtaining UI hierarchy XML file: com.android.ddmlib.SyncException: Remote object doesn't exist!
Error while obtaining UI hierarchy XML file: com.android.ddmlib.SyncException: Remote object doesn't exist!
        - 解决如下：
      ```commandline
        neil@NeildeMacBook-Pro ~ % ps -ef | grep appium
        501 14829 12900   0  2:01AM ??         0:00.00 /Applications/software/android-sdk-macosx/platform-tools/adb -P 5037 -s emulator-5554 shell am instrument -w io.appium.uiautomator2.server.test/androidx.test.runner.AndroidJUnitRunner
        501 14858 14846   0  2:02AM ttys002    0:00.00 grep appium
        neil@NeildeMacBook-Pro ~ % kill 14829
        neil@NeildeMacBook-Pro ~ % 
      
    -  MaxRetryError:
        - appium server 可能没打开

``` 
 
      
      

- appium执行速度优化
    - 1. 目前已知的导致速度慢的原因：
            
           -  使用xpath，在查找元素过程中尽量少用xpath
           - 用SetValue代替SendKey
            - 尽量少的和appium通讯
            - 使用driver.PageSouce先将页面缓存起来，找元素先去driver.PageSouce找
    
```python
cssSelector             # Selenium 最强大的定位方法，比 xpath 速度快，但比 xpath 难上手
linkText                # 链接元素的全部显示文字
partialLinkText         # 链接元素的部分显示文字
name                    # 元素的 name 属性，目前官方在移动端去掉这个定位方式，使用 AccessibilityId 替代
tagName                 # 元素的标签名
className               # 元素的 class 属性
id                      # 元素的 id 属性
xpath                   # 比 css 定位方式稍弱一些的定位方法，但胜在容易上手，比较好使用，缺点就是速度慢一些。
AccessibilityId         # Appium 中用于替代 name 定位方式
AndroidUIAutomator      # Android 测试，最强大速度最快的定位方式
iOSNsPredicateString    # iOS 谓词的定位方式，仅支持 XCTest 框架，需大于 iOS 9.3或以上
IosUIAutomation         # iOS 谓词的定位方式，仅支持 UIAutomation 框架，需大于 iOS 9.3或以下
iOSClassChain           # 国外大神 Mykola Mokhnach 开发类似 xpath 的定位方式，仅支持  XCTest 框架，，不如 xpath 和 iOSNsPredicateString 好
windowsAutomation       # windows 应用自动化的定位方式
```

### 元素属性和方法
    - 可以下源码用dndroid studio打开，搜索attribute
    

 ### 触屏自动化
    - 手势操作
        - 能拿元素尽量拿元素，拿不到就拿坐标点
        - 注意坐标点适配
        - 要release()和preferm（）

### 高级定位
    - xpath :

        查找股票这个选项
        
        - //*[@resource-id='com.xueqiu.android:id/title_container']/android.widget.TextView[last()-2]
           -  android.widget.TextView是class属性，相当于元素名
           -  resource-id 是id
        
        - //*[@resource-id='com.xueqiu.android:id/title_container']/android.widget.TextView[2]

         查找股票的父节点
        - //*[@resource-id='com.xueqiu.android:id/title_container']/android.widget.TextView[2]/..

        父子节点可以确认元素之间的关联性：
        比如阿里巴巴股票有很多只，当我只知道股票代码时，怎么确定这只股票对应的价格是哪个？可以通过父节点来确定
        - //*[@text='09988']/../../../*[@resource-id='com.xueqiu.android:id/price_layout']/android.widget.TextView[1]
            - //*[@text='09988']/../../..找到这个股票代码节点和股票价格有关联的父节点

    - 使用安卓自带的uiautomator定位：

        - 文档：https://developer.android.com/reference/android/support/test/uiautomator/UiSelector

        - 快，但表达式复杂，难用

### 显式等待

    - 问题：有了隐式等待为什么还要用显示等待呢？
        - 页面加载是有顺序的，比如web页面，他是从头head加载到css，js
            body，中间还有一些同步加载和异步的问题，比如图片，视频的加载就是异步加载
        - 手机app也是如此，框架先出来，图片视频后出来
        - 很多情况，元素已经加载出来，但是元素的属性，比如是否可见，是否可点击还没加载出来
        - 隐式等待只能确认元素出现在了dom树里（是否出现）了，但咩办法判断元素的属性
        - 显示等待的重点：判断是否可见，在深入一点，判断是否可点击
        
### toast控件的识别
    - 登陆成功一闪而过的提示框，就是toast，和alert，dialog不一样，需要特殊操作
    - toast是系统控件，不是app控件，需要特殊处理
    - 一般查找元素不建议使用class属性，但是toast例外

### 获取属性
    元素.get_attribute("")

### 断言框架 
    - hamcrest

### 参数化用例

### 纯web网页测试
    - 混合应用
        - 原生应用嵌套网页，解决app审核慢的问题，应用更新升级不再依赖原生审核平台，嵌套的网页开发和更新可以做到热更新，热启动


    - 如何知道模拟器用的是什么浏览器以及它的版本号？
        - 注意：不可以是第三方浏览器
        - 'Safari' for iOS and 'Chrome', 'Chromium', or 'Browser' for Android
        - 文档：https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/caps.md

        
```commandline
        # 获取所有包名
        adb shell pm list package
        # 获取浏览器包名
        neil@NeildeMacBook-Pro ~ % adb shell pm list package | grep browser
        # 获取浏览器版本信息
        neil@NeildeMacBook-Pro ~ % adb shell pm dump com.android.browser | grep version
              versionCode=23 targetSdk=23
              versionName=6.0.1
        neil@NeildeMacBook-Pro ~ % adb shell pm dump com.android.chrome | grep version
            
```

    - 根据浏览器的版本下载对应的浏览器驱动
        - 文档： https://raw.githubusercontent.com/appium/appium-chromedriver/master/config/mapping.json 找到对应的驱动
                https://github.com/appium/appium/blob/master/docs/en/writing-running-appium/web/chromedriver.md
        - 命令行下载驱动：
             npm install appium-chromedriver --chromedriver_version="2.24"
        -  常见报错：
            - Original error: No Chromedriver found that can automate Chrome '52.0.2743'
                - 命令行 npm server：npm install appium-chromedriver --chromedriver_version="2.24"
                这是命令行appium安装适配的driver，安装完，启动命令行appium server运行程序是咩有问题的
                - npm desktop:
                    - 下载对应版本的驱动，拷贝至目录：/Applications/Appium.app/Contents/Resources/app/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac/
                    https://chromedriver.storage.googleapis.com/index.html
                    - 这个目录是appium desktop自带的，如果我们不指定chromedriverExecutable路径，就会默认在这个目录找对应的driver
- 如何测试？
    - 使用谷歌自带的inspector
        - 谷歌浏览器输入：chrome://inspect/#devices
        - 因为使用的是相同的内核，可以同步模拟器的页面到浏览器上
    

### app 混合页面测试
    - 如何查看内嵌的是不是web页面？
        - 用uiaotumatorviewr查看,uiaotumatorview可以将webview渲染成本地组件，可以清楚看到webview标签，但是注意，渲染后的效果可能会和实际的有差别
        - 标准测试方式
    - 如何测试webview？
        - 需要跟开发沟通打开webview的debug开关
        - 打开以后，用chrome://inspect/#devices查看元素，切换上下文，其后所有的定位方式和selenium一样
        - 在原生页面嵌套的webview里面查找元素，要切换上下文
        - 在webview里面打开另一个webview，在另一个webview里面查找元素，要切换window
        - 原生页面获取窗口句柄，程序会报错
        

