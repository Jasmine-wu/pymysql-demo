import unittest
import time
# from Tool.HTMLTestRunner import HTMLTestRunner
from Tool.HTMLTestRunner_PY3 import HTMLTestRunner

class TestClass(unittest.TestCase):
    """
        整个类只执行一次setUpClass，tearDownClass
    """

    @classmethod
    def setUpClass(cls) -> None:
        print("call setUpClass01")
        cls.data =[0,1]
        print("name is ", __name__)

    @classmethod
    def tearDownClass(cls) -> None:
        print("call tearDownClass01")

    def setUp(self) -> None:
        print("call setUp01")

    def tearDown(self) -> None:
        print("call tearDown01")

    def test_01(self):
        self.assertEqual(TestClass.data[0], 0, "判读是否相等")

    def test_02(self):
        self.assertTrue(TestClass.data[1] < 2, "判读是否为真")


class TestClass02(unittest.TestCase):

    # @classmethod
    # def setUpClass(cls) -> None:
    #     print("call setUpClass02")
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     print("call tearDownClass02")

    def setUp(self) -> None:
        """
            每执行一条测试用例都执行一次set up，tear down
        """
        print("call setUp02")

    def tearDown(self) -> None:
        """
            清除缓存
            断开数据库连接
            清除资源文件等回收操作
        """
        print("call tearDown02")

    def test03(self):
        self.assertEqual(0, 0, "判读是否相等")

    # 跳过此条测试用例不执行，可带条件
    # @unittest.skip
    @unittest.skipIf(1 + 1 == 2,"reason")
    def test_02(self):
        self.assertTrue(1<2, "判读是否为真")

if __name__ == '__main__':

    # 执行当前模块所有测试用例
    # unittest.main()

    # 执行多个测试用例
    # suit = unittest.TestSuite()
    # suit.addTest(TestClass("test_01"))
    # suit.addTest(TestClass02("test_02"))
    # runner = unittest.TextTestRunner()
    # runner.run(suit)

    # 执行多个测试类
    # suit1 = unittest.TestLoader().loadTestsFromTestCase(TestClass)
    # suit2 = unittest.TestLoader().loadTestsFromTestCase(TestClass02)
    # suits = unittest.TestSuite([suit1, suit2])
    # unittest.TextTestRunner().run(suits)


    # 加载路径下所有测试用例
    suits = unittest.defaultTestLoader.discover("./", pattern="unittest*.py")
    # unittest.TextTestRunner().run(suits)

    #生成测试报告
    file_name = "./Report/{}.html".format(time.strftime("%Y%m%d-%H%M%S",time.localtime()))
    # print(file_name)
    with open(file_name, "wb") as f:
        # HTMLTestRunner.run(suits)
        runner = HTMLTestRunner(f, title=" 测试报告")
        runner.run(suits)