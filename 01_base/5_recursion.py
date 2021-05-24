from functools import lru_cache


# 递归是一种分层推导解决问题的方法
# 编写递归函数有两个要点：
# 出口条件，可以不止一个
# 推导方法（已知上一个结果怎么推导当前结果）

# 阶乘factorial
def factorial(n):
    if n == 1:  # 出口
        return 1
    return factorial(n - 1) * n


# 优化fib(n-2)其实计算了两次：可以通过缓存来优化效率
@lru_cache()
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# 跳台阶：一只青蛙，一次可以跳上1阶，也可以跳上2阶，问跳上n阶有多少种跳法
# 跳台阶实际上就是一个从第二位开始的斐波那切数列：1 2 3 5 8 13 ...
def jump1(n):
    if n <= 2:
        return n
    return jump1(n - 1) + jump1(n - 2)


# 变态跳台阶：一只青蛙，一次可以跳上1阶，可以一次跳上n阶，为跳上n阶有多少种跳法。
# 变态跳台阶只是推导方式不同，每一层的结果是上一层跳法的2倍。
def jump2(n):
    if n <=2:
        return n
    return jump2(n-1) *2


if __name__ == '__main__':
    # print(factorial(5))
    # print(fib(5))

    jump3 = lambda n: n if n <= 2 else jump3(n - 2) + jump3(n - 1)
    jump4 = lambda n: n if n <= 2 else jump4(n - 1)*2

    # print(jump1(10))
    print(jump2(10))
    print(jump4(10))


