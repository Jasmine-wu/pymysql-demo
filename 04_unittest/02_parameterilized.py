import unittest
from parameterized import parameterized

data_add = [(1,2,3), (2,2,4), (4,4,8)]
# data_add = ['1','2','3']

def add(x,y):

    return x + y

class Test02(unittest.TestCase):

    @parameterized.expand(data_add)
    def test_add(self, x, y, expect):
        result = add(x,y)
        self.assertEqual(result, expect)

    # @parameterized.expand(data_add)
    @unittest.skip('未完成的代码')
    def test_add2(self, num):


        print('num is :', num)


    # def test_add2(self):
    #     result = add(1,5)
    #     print('result01 is :', result)


# if __name__ == '__main__':
#     print(__name__)
#     unittest.main()
