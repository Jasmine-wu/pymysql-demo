# 传参
# args和kwargs组合起来可以传入任意的参数
def args_kwargs1(first, *args,**kwargs):
    print('Required argument: ', first)
    print(type(args))
    print(type(kwargs))

    #  args是一个元祖，里面接收的是非关键字参数列表（2,'xxx', {"key":1}）
    for v in args:
        print ('Optional argument: ', v)
    # kwargs是一个字典，接收关键字参数
    print(kwargs) # {'zhangsan': 29, 'lisi': 2}

def args_kwargs2(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

if __name__ == '__main__':
    # 传参
    args_kwargs1(1, 2,'xxx', {"key":1}, zhangsan=29, lisi=2)

    # 解包
    a = ( 2,'xxx', {"key":1})
    args_kwargs2(*a)

    # 注意这里key值必须跟参数是一样的
    b = {"arg3": 3, "arg2": "two", "arg1": 5}
    args_kwargs2(**b)






