# 写一个斐波那契数列
# F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)
def fib(n):
    if isinstance(n, int):
        if n < 0:
            return
        if n <= 1:
            return n
        return fib(n - 1) + fib(n - 2)

if __name__ == '__main__':
    print(fib("**"))
    print(fib("str"))
    print(fib(-10))

    print(fib(0))
    print(fib(0.1))
    print(fib(1))

    print(fib(5))
