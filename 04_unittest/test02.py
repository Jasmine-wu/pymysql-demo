import unittest
def add(x,y):
    return x + y

class Test02(unittest.TestCase):
    def test_add(self):
        result = add(1,2)
        print('result02 is :', result)
        print('__name__', __name__ )

    def test_add2(self):
        result = add(1,5)
        print('result02 is :', result)


if __name__ == '__main__':
    print(__name__)
    unittest.main()
