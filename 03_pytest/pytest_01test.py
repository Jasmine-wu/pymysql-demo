"""
    pytest 丰富的包
    - 运行过程的界面美化

    // 失败重新运行
    测试失败后要重新运行n次，要在重新运行之间添加延迟时间，间隔n秒再运行。
    pip install pytest-rerunfailures
    pytest --reruns 3 -v -s filename
    pytest -reruns 3 --reruns-delay 1
    - 多任务并发执行测试用例

    //一条测试用例多条断言有失败也运行
    一个场景中有多条断言方法，通常第一条过不去，下面就不执行了，我们想报错也执行一下
    - pip install pytest-assume
    pytest.assume(断言表达式)
    pytest.assume(1=4)

    //pytest-fixture
    - 用例1需要登陆
    - 用例2不需要登陆
    - 用例3需要登陆
    这种场景用setup teardown 是无法实现的
    解决： 在登陆方法前面加 pytest.fixture(),作用范围是类外的function测试方法，调用需要在参数里传入方法名，类里面测试方法传入不起作用

    //pytest提供了公共文件conftest.py，可以将常用的模块放到这个文件里
        注意：conftest和测试方法要在同一个pakage下

    //测试方法销毁清除数据如何处理？ 范围是模块级别的，默认作用域是function
    @pytest.fixture(scope="module") 与 yeild搭配使用
def open():
    print("这是一个open方法该测试用例执行前调用")
    yield
    print("这是一个open方法所有测试用例执行后调用") 相当于setup_module teardown_module

    // pytest的自动运用 @pytest.fixture(autouse=True)
    不需要从参数中导入函数，作用于所有测试方法

    //fixure带参数，传入数据
    //fixure带参数，传入函数和数据


    //setUp tearDown 更灵活
    模块setUp_module-》函数级（类外）function-》类级class-》方法级 menthod（类中）-》类里面的 setUp


    //跳过某条测试用例
    @pytest.mark.skip(msg)

    //执行部分特定测试用例：打标签
     - @pytest.mark.markername
     - 在conftest里重写def pytest_configure(config):

     //多线程并行和分布式执行测试用例
     - pip install pytest-xdist
     - 多个cpu一起并行执行 -n 3 指定3个cpu
         前提是，测试用例是相互独立的，没有先后执行顺序，随即都能执行
         pytest filename -n 3

    // 生成测试报告(并不美观，需改进)
    - pip install pytest-html
    - pytest -v -s filename --html=report.html --self-contained-html
    - 改进用pytest-allure
        安装：
        - brew install allure
        - pip3 intall allure-pytest
        生成：
          - pytest --alluredir=指定测试生成测试报告路径 生成测试数据
            pytest pytest_01test.py --alluredir=./report
          - allure serve 指定测试生成测试报告路径       用测试数据生成测试报告
           // 在线生成，生成立马打开
            allure serve ./report

          // 生成并保存到指定目录，然后手动打开
             -clean: 覆盖
            allure generate ./report -o ../Report -clean
            allure open -h 127.0.0.1 -p 8833 ../Report





    pytest 会自动收集以test_为开头的文件
    - 测试类要以Test开头
    - 测试方法要以test_开头

-v 更详细打印日志
    pytest -v -s pytest_01.py
    pytest pytest_01.py::Test_01
    pytest pytest_01.py::Test_01::test_001
    //skip
    pytest pytest_01.py -k "Test_01 and not test_001"

//一旦运行报错就停止运行
    pytest -x filename 

//当运行错误达到num就停止运行
    pytest --maxfail=[num] 

//执行某部分测试用例，在测试方法前加 @pytest.mark.标记名
    pytest -m 标记名
    

   pytest 运行高级用法
    - pytest 运行规则是可修改的 
    - 运行包含add的测试用例 pytest -v -k "add"
        collected 4 items / 1 deselected / 3 selected                                                                                                          
        test_calc.py::TestCalc::test_add_1 PASSED                                                                                                        [ 33%]
        test_pytest01.py::TestCalc::test_add PASSED                                                                                                      [ 66%]
        test_pytest01.py::TestCalc::test_add1 PASSED  
        
    - 运行包含add和div的测试用例  pytest -v -k "add or div"
       collected 5 items                                                                                                                                      

    test_calc.py::TestCalc::test_add_1 PASSED                                                                                                        [ 20%]
    test_pytest01.py::TestCalc::test_add PASSED                                                                                                      [ 40%]
    test_pytest01.py::TestCalc::test_add1 PASSED                                                                                                     [ 60%]
    test_pytest01.py::TestCalc::test_div PASSED                                                                                                      [ 80%]
    test_pytest01.py::TestCalc::test_01div PASSED      
                                                                                                     [100%]
    - pytest  collection收集规则是可改变的
     - pyetst --collect-only 仅仅收集，不run，可用来统计有多少条测试用例
        
    -  pytest -v -k "jian"
    -  pytest -vs -m jian

pytest --help | pbcopy


"""
import pytest
import sys
import yaml

# 这个公共方法可以放到公共文件conftest里
# @pytest.fixture()
# def login():
#     print("这是一个login方法===================")


"""
参数化================
"""


# 传入数据
@pytest.mark.parametrize("test_input,expected", [("1+1", 2), ("1+2", 3), ("1+3", 4)])
def test_06(test_input, expected):
    # eval将字符串当成表达式求值
    assert eval(test_input) == expected


@pytest.mark.parametrize("x", [1, 2, 3])
@pytest.mark.parametrize("y", [2, 3])
def test_07(x, y):
    # eval将字符串当成表达式求值
    assert x + y > 0


# 传入函数和数据 indirect=True,可以把传入的参数当函数执行
# login_data = {"username":"zangsan","password":"123456"}
login_data = [{"username": "zangsan", "password": "123456"}]


@pytest.fixture(scope="module")
def login_01(request):
    params = request.param
    print(params)

    return "这里是函数的返回值"


@pytest.mark.parametrize("login_01", login_data, indirect=True)
def test_08(login_01):
    a = login_01
    print("打印函数的返回值", a)


"""
  yaml 文件参数化
        - pip install pyyaml
        - import yaml
"""


@pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("./data.yaml")))
# @pytest.mark.parametrize(["a","b"], yaml.safe_load(open("./data.yaml")))
# @pytest.mark.parametrize("a,b", yaml.safe_load(open("./data.yaml")))
def test_yaml(a, b):
    assert a + b > 0


def test_04(open):
    print("test-04中open方法调用==================")
    assert "a" in "ac"


def setup_module():
    print("set up module")


def tear_module():
    print("tear down module menthod")


def setup_funtion():
    print("setup function menthod")


def teardown_function():
    print("setup funtion menthod")


class Test_01():
    def setup_class(self):
        print("setup_class ")

    def teardown_class(self):
        print("teardown_class ")

    def setup_menthod(self):
        print("setup menthod ")

    def teardown_menthod(self):
        print("teardown menthod ")

    def setup(self):
        print("setup ")

    def teardown(self):
        print("teardown")

    def test_001(login):
        print("这是需要login，但是login不起作用")
        assert "a" in "abc"

    @pytest.mark.test1
    def test_002(self):
        print("call test_02")
        assert "a" in "abc"


@pytest.mark.test1
class Test_02():
    def test_003(self):
        print("call test_003")
        assert "a" in "abc"

    def test_004(self):
        print("call test_004")
        assert "a" in "abc"
        pytest.assume('a' in 'acc')


@pytest.mark.test1
def test_03(login):
    print("test-03需要登陆")
    assert "a" in "abc"


"""
    skip加条件
"""


# @pytest.mark.skip("这条暂时不执行")
@pytest.mark.skip(sys.platform == 'darwin', reason="不在macos上运行")
class Test_05():

    def test_005(self):
        print("call test_005")
        assert "a" in "abc"
        pytest.assume('a' in 'acc')


@pytest.mark.xfail
class Test_010():
    def test_010(self):
        assert "a" not in "abc"


# # 点这里的绿箭头可以执行所有的测试用例
if __name__ == '__main__':
    print("==========================================")
    pytest.main(['-v', '-x', 'pytest_01.py::Test_02::test_003'])
