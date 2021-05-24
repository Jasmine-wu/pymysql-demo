"""
    装饰器,把相同的内容抽走
    用于扩展函数
    args接受了所有普通参数，kwargs接收所有关键字参数
    *args, **kwargs 代表了所有参数
"""

# 定义一个扩展函数
def extend(func):
    # 必须这样写(*args, **kwargs)

    def zhuangshiqi(*args, **kwargs):
        print("hello")
        print(args)
        print(kwargs)
        # 调用被装饰的函数
        func(*args, **kwargs)
        print("bye")

    #调用装饰器本身
    return zhuangshiqi

@extend
def tmp(a,b,c):
    # print("hello")
    print("tmp")
    # print("bye")
@extend
def tmp1():
    # print("hello")
    print("tmp1")
    # print("bye")

def test_wrapper():

    # tmp()
    # tmp1()

    # extend(tmp)()
    # extend(tmp1)()

    tmp(1.0,b=2, c=1)

    # tmp1()

