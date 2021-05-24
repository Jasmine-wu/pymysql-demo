num = 9
def f1():
    num = 20

def f2():
    print(num)
f2()  # 9
f1()  # 啥也没有
f2()  # 9

# 如果想要输出 9 20 ，要如何做？
def f1():
    global num
    num = 20

def f2():
    print(num)

f2()  # 9
f1()  # 啥也没有
f2()  # 20


def strtest1(num):
    str='first'
    print(id(str))
    for i in range(num):
        str= str+"X"
        print(id(str))
    return str
strtest1(5)