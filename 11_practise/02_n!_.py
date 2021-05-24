#  n的阶乘

def f(n):
    if isinstance(n, int) and n >= 0:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return f(n - 1) * n


if __name__ == '__main__':
    print(f('99$'))
    print(f('&&'))
    print(f('ddd'))
    print(f(-1))
    print(f(0.1))
    print(f(0))
    print(f(1))
    print(f(5))
