# 如何优化得到想要的结果
# def multipliers():
#     return [lambda x: i * x for i in range(4)]
## print([m(2) for m in multipliers()])  # [6, 6, 6, 6]

# ==============还原==============
# 还原lanbda
la = lambda x: x * 2

def f(x):
    return x * 2

# 还原：
# def multipliers():
#     return [lambda x: i * x for i in range(4)]
def multipliers():
    result = []
    for i in range(4):
        def f(x):
            return x * i
        result.append(f)
    return result
f1,f2,f3,f4 = multipliers()
print(f1(2))
print(f2(2))
print(f3(2))
print(f4(2)) # 6 6 6 6

# 改进2：===============================
# 怎么把i值保存下来？
# 把i值传到闭包函数里
def multipliers():
    result = []
    def g(i):
        def f(x):
            return x * i
        return f
    for i in range(4):
        result.append(g(i))
    return result

f1,f2,f3,f4 = multipliers()
print(f1(2))
print(f2(2))
print(f3(2))
print(f4(2))

# 改进1：================================
#  直接把for循环放到闭包函数里
def multipliers():
    result = []

    def inner(x):
        for i in range(4):
            result.append(i * x)
        return result

    return inner

m = multipliers()
print(m(2))  # [0, 2, 4, 6]

#
