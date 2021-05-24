

class Counter:
    #  必须加func参数
    def __init__(self,func):
        # self.func = func
        # 记录调用次数
        self.count = 0

    #  实现了这个函数，实例会变得可调用callable(dog)=True，没实现，为false
    #  类可以记录数据，可以利用这个特性，实现类装饰器，记录函数被调用的次数
    def __call__(self, *args, **kwargs):
        print("*args",args)
        print("**kwargs",kwargs)

        self.count += 1
        # return self.func(*args, **kwargs)

# 类装饰器： call_func会作为类装饰器初始化的一个参数传进入
@Counter
def call_func(a,b,c):
    print(a)
    print(b)
    print(c)

for i in range(10):
    call_func(2,"str", {"key":10})
    print(call_func.__class__)

print(call_func.count)


