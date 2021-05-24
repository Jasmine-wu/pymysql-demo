import sys
import pytest

"""
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
    
    -  pytest --junit-xml=./result 生成xml格式测试报告
       网上很多格式化软件 bejson.com 
       https://www.bejson.com/jshtml_format/
    
    <?xml version="1.0" encoding="utf-8"?>
<testsuites>
	<testsuite name="pytest" errors="0" failures="0" skipped="0" tests="8" time="0.080" timestamp="2021-03-14T21:58:18.976856" hostname="NeildeMacBook-Pro.local">
		<testcase classname="test_calc.TestCalc" name="test_add_1" time="0.001" />
		<testcase classname="test_pytest01.TestCalc" name="test_add" time="0.001" />
		<testcase classname="test_pytest01.TestCalc" name="test_add1" time="0.001" />
		<testcase classname="test_pytest01.TestCalc" name="test_div" time="0.001" />
		<testcase classname="test_pytest01.TestCalc" name="test_01div" time="0.001" />
		<testcase classname="test_pytest01.TestCalc" name="test_jian3" time="0.001" />
		<testcase classname="test_pytest01" name="test_jian1" time="0.001" />
		<testcase classname="test_pytest01" name="test_jian2" time="0.001" />
	</testsuite>
</testsuites>


- pytest测试用例执行顺序
    - 按顺序执行，写在前面的先执行
- unittest测试用例执行顺序：它会以用例名字的ACSII码值的顺序来执行

- 我们想改变pytest测试用例执行顺序应该怎么做？
    - 单元测试的规范就是不允许有顺序，会给你自定义一个顺序，按照系统的顺序执行
      代码测试的时候最好不要有顺序，集成测试是可以有顺序的，
      代码层面是不允许有顺序的，有顺序的有上下依赖关系，这种情况要进行拆解
    - 设计自动化测试还不推荐像集成测试那样有逻辑依赖的，最好也不要顺序，但是很多写自动化测试代码的习惯有个逻辑。
       pytest.order 可以做到自定义顺序. 一般集成测试才会用!!!!
        - 安装
            pip3 install pytest-ordering
        - @pytest.mark.run(order=1) /   @pytest.mark.first
            @pytest.mark.run(order=-1) 倒数第二个执行

        - 或者重写排序的方法
    

"""
sys.path.append("..")
#
# print("asdfadnfadfnaldskfnal;ksdfna;lsfkdnalfna;dfnasfdkn")
# print("===sys.path=======",sys.path)

from python.calc import Calc


class TestCalc():

    # python3.5以后的新特性 type hints类型提示

    def test_add(self):
        self.calc = Calc()
        result = self.calc.add(1, 2)
        assert 3 == result

    @pytest.mark.first
    # @pytest.mark.run(order=1)
    def test_add1(self):
        self.calc = Calc()
        result = self.calc.add(1, 2)
        assert 3 == result

    def test_div(self):
        self.calc = Calc()
        assert 2 == self.calc.div(2, 1)

    @pytest.mark.second
    # @pytest.mark.run(order=2)
    def test_01div(self):
        self.calc = Calc()
        assert 2 == self.calc.div(2, 1)

    @pytest.mark.run(order=-1)
    def test_jian3(self):
        assert 2 == 2

@pytest.mark.run(order=3)
@pytest.mark.jian
def test_jian1():
    assert 2 == 2


@pytest.mark.jian
def test_jian2():
    assert 2 == 2

# def pytest_co


"""
    python的入口函数
    没有入口函数，也可以直接调用pytest.main
"""
if __name__ == '__main__':
    # 没生效，执行了所有的测试用例，why？IDE自己的问题
    # if __name__ == '__main__': 是用pyhton自己的解释器来执行的，代表执行的是个python文件而不是pytest文件
    # 而run pytest for xxx，是以pytest解释器运行的
    # 如何做？重新config，删除掉其他config，新建一个python的config，配置脚本路径（要用python解析器执行的文件）

    # ['-vs', 'test_pytest01.py::TestCalc::test_add'] 要用list方式，字符串方式在高版本中已废弃
    pytest.main(['-vs', 'test_pytest01.py::TestCalc::test_add'])


