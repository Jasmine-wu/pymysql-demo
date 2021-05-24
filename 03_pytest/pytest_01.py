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
    解决： 在登陆方法前面加 pytest.fixture(),作用范围是类外的function测试方法，类里面测试方法传入不起作用

    //pytest提供了公共文件conftest.py，可以将公共代码放到这个文件里

    //setUp tearDown 更灵活
    模块setUp_module-》函数级（类外）function-》类级class-》方法级 menthod（类中）-》类里面的 setUp

    - 完美测试报告
"""

"""
    - 测试类要以Test开头
    - 测试方法要以test开头
"""

"""
pytest -v -s pytest_01.py
pytest pytest_01.py::Test_01
pytest pytest_01.py::Test_01::test_001
//skip
pytest pytest_01.py -k "Test_01 and not test_001"

//一旦运行报错就停止运行
pytest -x filename 

//当运行错误达到num就停止运行
pytest --maxfail=[num] 

//运行有这个标记的测试用例 @pytest.mark.标记名
pytest -m 标记名

"""
import pytest


@pytest.fixture()
def login():
    print("这是一个login方法===================")


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

    def test_002(self):
        print("call test_02")
        assert "a" in "abc"


class Test_02():
    def test_003(self):
        assert "a" in "abc"

    def test_004(self):
        print("call test_02")
        assert "a" in "abc"
        pytest.assume('a' in 'acc')


def test_03(login):
    print("test-03需要登陆")
    assert "a" in "abc"


# # 点这里的绿箭头可以执行所有的测试用例
if __name__ == '__main__':
    print("===============9878907===========================")
    pytest.main(['-v', '-x', 'pytest_01.py::Test_02::test_003'])
