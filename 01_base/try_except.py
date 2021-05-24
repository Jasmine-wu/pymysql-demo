
# 捕捉异常，代码可以继续执行
def try_cat():
    try:
        a = int(input("请输入一个除数"))

        b = int(input("请输入一个被除数"))

        print(a/b)

    except ZeroDivisionError:
        print("被除数不能为0")
    except ValueError:
        print("请输入整数")
    except Exception as result:
        print("打印为止异常")
        print(result)
    else:
        print("没有异常执行的代码快")
    finally:
        print("异常或者正常都会调用")

# 主动抛出异常
# 不捕捉异常，一旦出现异常，代码运行会停止
def raiseE():

    print("开始")
    raise Exception("这是一个异常")
    #异常未捕捉，这样代码不会执行
    print("结束")

# raiseE()

def user_input():
    try:
        a = int(input("请输入除数"))
        b = int(input("请输入被除数"))
        f = input("请输入+——*%")
        if f != "+" and f != "-" and f != "*" and f != "/" :
            raise Exception("请输入正确的运算符+-*/")
        if f == "/":
            num = a/b
            print(num)
    except Exception as result:
        print(result)

user_input()