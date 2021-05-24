import time
import threading
class Dog:
    #  对象创建时调用
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = object.__new__(cls)
        return cls._instance

    # 对象初始化时调用
    def __init__(self, name, age):
        self.name = name
        self.age = age
        time.sleep(2)

    #  实现了这个函数，实例会变得可调用callable(dog)=True，没实现，为false
    def __call__(self, *args, **kwargs):
        pass

    # 对象销毁时调用
    def __del__(self):
        print("del call")


# 但是这样创建的单例在单线程是没问题的，但是遇到多线程就会出问题
def create():
    dog = Dog("zhang", 11)
    print(dog)
    print(callable(dog))

#  好像没啥问题啊=》在init方法里加sleep制造线程阻塞看看=>也没啥问题啊------
for i in range(10):
    t = threading.Thread(target=create(), args=[i, ])
    t.start()

