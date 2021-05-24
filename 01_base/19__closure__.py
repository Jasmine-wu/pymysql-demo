
# 闭包

# ========================
# 嵌套函数，变量作用域
num = 20
def foo():
    num1 = 10 # 局部变量
print(num)
# print(num1) 报错

# ========================
# def a():
#     msg = "this is A"
#     def b():
#         print(msg)
#     b()
# a()
# ========================

# 闭包
# 必包函数返回的是内函数
# 内函数引用了外函数的外部变量，这个内函数就叫必包
def add(a):
    x = 100
    print(x)
    def b(b):
        x = 120
        print("inner x:",x)
        return a * b
    print("outer x:", x)
    return b

# 外部函数
# 外部函数在结束的时候发现有自己的临时变量将来会在内部函数中用到，就把这个临时变量绑定给了内部函数，然后自己再结束。
# 闭关函数无法修改外函数的局部变量

a = add(10)
print(a(20))
print(a.__closure__)

# 闭关函数也无法直接访问外函数局部变量
# def add2():
#     x = 1
#     def b():
#         x = x +1
#         return x
#     return b
# a = add2()
# a()

# 但是可以通过容器访问,因为容器类型不是存放在栈空间的
def add3():
    x= [100]
    def b():
        x[0] = x[0] +1
        return x[0]
    return b
a = add3()
print(a())

#  也可以通过
def add2():
    x = 1
    def b():
        nonlocal x # 申明x为非局部变量
        x = x +1
        return x
    return b
a = add2()
print(a())


#=====================================
# def call_sum(*args):
#     ax = 0
#     for n in args:
#         ax = ax + n
#     return ax
# print(call_sum(1, 2, 3))

# 改造成闭包函数
def call_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

sum1 = call_sum(1,2,3)
print(sum1())

sum2 = call_sum(1,2,3)
print(sum2())
print(sum1 == sum2)
print(id(sum1))
print(id(sum2))

# =============================
def count():
    fs = []
    for i in range(1, 4):
        def f():         # 返回函数f()放在循环里
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
# 9 9 9
print(f1())
print(f2())
print(f3())

# 改进
def count():
    fs = []
    def g(i):
        def f():
            return i*i
        return f
    for i in range(1, 4):
        fs.append(g(i))
    return fs
f1, f2, f3 = count()
# 1 4 9
print(f1())
print(f2())
print(f3())

#  lambda函数
temp = lambda x :x * 2
print(temp(2))
# 等效于
def temp(x):
    return x *2
print(temp(2))

#=============================
# 笔试题1
def fun():
    temp=[lambda x:x*i for i in range(4)]
    return temp
for every in fun():
    print(every(2))
# 输出 6 6 6 6

# 笔试题2
def mulby(num):
    def gn(val):
        return num * val
    return gn
zw = mulby(7)
print(zw(9))
# 输出 63

#+++++++++++++++++++++++++++++++++
# 闭包在数据处理，计算多组值时优势就体现出来
# 用闭包处理数据 y = a * x + b
def y(a, b):
    def inner(x):
        return a*x+b
    return inner
y1 = y(1,2)
y2 = y(2,4)

print(y1(1))
print(y1(2))

print(y2(4))
print(y2(5))
