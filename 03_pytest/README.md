## pytest
- pytest运行规则

pytest默认会收集test_*.py文件，Test开头的类，以test——开头的函数或者方法

- pytest常用参数

 --collect-only：只收集测试用例，不执行，可用于统计有多少测试用例

-m markname： 加标签，过滤执行标签为markname的测试用例,用例加@pytest.mark.markname,
执行：pytest -m markname

--junit-xml ：生成一个执行结果的xml文件，格式化可用bejason网站

-k xx ：执行含有xx的测试方法，例如 pytest -k add

-v：详情输出

-s： 打印print

- conftest.py文件
    - 重写pytest_configture方法添加标签去除警告
    - 重写排序方法pytest_collection_modifyitems，修改排序规则
    - 放置公共方法，数据，fixture方法等
    

- pytest.ini pytest setting的配置文件

 主要是改变pytest的运行规则：

```buildoutcfg
[pytest]
python_files = 'abc*.py'
python_classes = 'ab*'
python_functions = 'add*'
addopts = -vs --alluredir ./report

```

- pytest.ini文本文件必须以[pytest]开头
- pytest默认执行test*开头的文件，Test_和test_开头的类和测试用例，这个规则是可改变的
- python_files = 'abc*.py' pytest会默认运行abc开头的py文件
- python_classes = 'ab*' 运行以ab开头的类
- python_functions = 'add*' 运行以add开头的测试方法
- addopts = -vs --alluredir ./report  运行pytest等同于运行pytest -vs --alluredir ./report


- 导出依赖包

``pip freeze > requriments.txt
``

- 帮助文档复制

``pytest --help | pbcopy``

- 数据驱动 - 测试数据

  - @pytest.mark.parametrize("a,b, expect", [
    ('1', '2', '3'),
    ('0.1', '0.2', '0.3'),
    ('0', '1', '1')
])
    
def test_add_04(a, b, expect):
    result = Decimal(a) + Decimal(b)
    assert result == Decimal(expect)
    
浮点型的精度问题： 0.3 != 0.30000000
   from decimal import Decimal
   Decimal('1')+Decimal('2')

-  数据驱动 - 测试步骤
    
- pytest fixture高级用法
 
    - yeild生成器，相当于return+暂停+记住上一次运行的位置，和fixture连用，激活yeild
后面的操作
      
       - yield关键字用来定义生成器（Generator），其具体功能是可以当return使用，从函数里返回一个值，不同之处是用yield. 也就是说，yield返回函数，交给调用者一个返回值，然后再“瞬移”回去，让函数继续运行， 直到吓一跳yield语句再返回一个新的值
       - yeild的问题，当setup有异常，yield后面是不会执行的，可以用request.addfinalizer来完成一些teardown操作
      
    - fixture 执行优先级：secssion是最高级别，最低级是function，autouse大于同级，不管谁先调用
        - --setup-show 参数可以看出每个用于fixture执行顺序
      
    - 终结器
    - 工厂模式
    - 反射
        - print(getattr(zhansan, "drink","100"))，获取对象的属性或者方法，有就获取值，没有获取值
        - print(getattr(zhansan, "drink"))


## Allure
    - 安装：
        - mac linux按官网安装
        - windows 下载zip包
        - allure-pytest pyhton第三方库，不安装无法识别--alluredir命令
            allure52版本以上需要jdk1.8版本
    
    - 生成html报告
        - allure generate ./report
        - allure open ./report
    - 生成jason
        - pytest --alluredir ./report

    - allure提供的API
        - 添加操作步骤，features，stories，图片，html，文字，链接