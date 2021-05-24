# 装饰器让你在一个函数的前后去执行代码。
from functools import wraps
def wrapper(func):
    # 解决name的问题
    @wraps(func)
    def inner(*args, **kwargs):
        print("before func() call", func)
        func(*args, **kwargs)
        print("after func() call", func)
    return inner

@wrapper
def log():
    print("print log")

log()
# log.__name__应该是log,但是这里却是inner
print(log.__name__)

# 如何解决name的问题？functools @wraps(func)
print(log.__name__)
