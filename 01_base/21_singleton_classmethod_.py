import threading
import time

# 类方法创建
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        time.sleep(10)

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if not hasattr(Dog, '_instance'):
            Dog._instance = cls(*args, **kwargs)
        return Dog._instance

# 这样创建调用的是init方法，是不会得到单例的
dog1 = Dog("zhang", 11)
print(id(dog1))
dog2 = Dog("Li", 22)
print(id(dog2))

# 这样创建的才是单例
dog3 = Dog.get_instance("zhang", 11)
dog4 = Dog.get_instance("li", 22)
print(id(dog3))
print(id(dog4))


# 但是这样创建的单例在单线程是没问题的，但是遇到多线程就会出问题
def create():
    dog = Dog.get_instance("zhang", 11)
    print(dog)

#  好像没啥问题啊=》在init方法里加sleep制造线程阻塞看看=>也没啥问题啊------
for i in range(10):
    t = threading.Thread(target=create(), args=[i, ])
    t.start()
