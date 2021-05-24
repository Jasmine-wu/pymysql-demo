"""
    - 3.3 版本以前：conftest.py文件和运行的文件要在同一个package下，且需要__init__文件才能调用到里面的模块
    conftest文件在3。3版本以后不需要__init__.py文件，也可以调用，
    为了统一,版本兼容，都加上__init__.py文件.
    -  本层conftest优先级最高，当本层conftets文件调用不到，才会往上调用上层的conftest文件
       如果本层有conftest文件，外层也有，会优先调用本层的
    - conftest.py文件名不能改，是固定的

    - @pytest.mark.markname 经常出翔警告，如何解决？
      在conftest文件里重写：
      def pytest_configure(config):
         markerlist = ["test1", "login1"]
        for mark in markerlist:
            config.addinivalue_line("markers", mark)

    作用：
        - 可以共享数据，方法，fixture方法写在这个文件里
        - 重写执行方法，改变执行顺序
        - 重写pytest_configure方法，添加标签

"""

import pytest

"""
@pytest.fixture() 默认是scope是funciton级别
"""


@pytest.fixture()
def login():
    print("这是一个login方法===================")


"""
@pytest.fixture(scope="module") 和yeild配合使用相当于添加了一个模块级的setup tear dowm方法
全模块只调用一次，yield 之前是调用该方法的测试方法执行前调用
yield之后所有测试方法执行完之后调用
yield 相当与 return 默认是没有返回值的
"""
# @pytest.fixture(scope="module")
# def open():
#     # 这是加测试方法执行前的操作
#     print("这是一个open方法测试方法执行前调用")
#
#     # yield 默认是没有返回值的，希望有返回值 + addfinalizer
#     yield
#     # 这是加模块执行完以后数据销毁操作
#     print("这是一个open方法所有测试方法执行后调用")
#
# @pytest.fixture(autouse=True)
# def open_02():
#     print("这是open_02方法的自动应用, 即使不导入，所有测试方法执行前都会调用")

# @pytest.fixture(params=['1','2','3','india'])
# def test_data(request):
#     return request.param


"""
    重写pytest_configure避免warning
"""

def pytest_configure(config):
    markerlist = ["test1", "login1"]
    for mark in markerlist:
        config.addinivalue_line("markers", mark)
