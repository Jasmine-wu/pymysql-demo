class A(object):

    def __call__(self, *args, **kwargs):
        print("call A")

if __name__ == '__main__':

    a1=A()
    #  怎么让这行代码跑起来，即对象实例被调用起来
    a1(80)