#
from functools import lru_cache
# from  requests_html import HTMLSession
import time


# lru_cache装饰器会记录以往函数运行的结果，实现了备忘（memoization）功能
# 避免参数重复时反复调用，达到提高性能的作用，在递归函数中作用特别明显

# 不带参数
@lru_cache()
def console1(a, b):
    print("进入函数")
    return (a, b)
print(console1(3, 'a'))
print(console1(2, 'b'))
print(console1(3.0, 'a'))  # 没打印，why？

print("*"*50)
# 带参数(maxsize可以缓存最多个此函数的调用结果)
# 参数maxsize为最多缓存的次数，如果为None，则无限制，设置为2的n次幂时，性能最佳；
# 如果 typed=True，则不同参数类型的调用将分别缓存，例如 f(3) 和 f(3.0)，默认False
@lru_cache(maxsize=128, typed=True)
def console1(a, b):
    print("进入函数")
    return (a, b)
# print(console1(3, 'a'))
# print(console1(2, 'b'))
# print(console1(3.0, 'a'))  # 打印了

# 优化fib(n-2)其实计算了两次：可以通过缓存来优化效率
#  优化时间真的很明显。。。。。。。。。
@lru_cache()
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# 手动缓存优化(达到的效果跟lru_cache差不多)
cache = {}
def fib2(n):
    if n in cache.keys():
        return cache[n]
    if n <= 1:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)
    cache[n] = result
    return result


# 爬虫的去重操作，避免网页的重复请求
# session=HTMLSession()
# @lru_cache()
# def get_html(url):
#     req=session.get(url)
#     print(url)
#     return req
#
# urllist=["https://www.baidu.com","https://pypi.org/project/pylru/1.0.9/","https://www.baidu.com"]
#
if __name__ == '__main__':
    # for i in urllist:
    #     print(get_html(i))

    # start_time = time.time()
    # print(fib2(200))
    # print("time:", time.time() - start_time) # 0.00027298927307128906

    start_time = time.time()
    print(fib(200))
    print("time:", time.time() - start_time) #  0.0002689361572265625
