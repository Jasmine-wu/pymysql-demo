class B():
    def fn(self):
        print('B fn')
    def __init__(self):
        print("B INIT")

class A():
    def fn(self):
        print('A fn')

    def __new__(cls, a):
        print("NEW", a)
        if a > 10:
            # 返回自身实例的另种写法
            # return super(A, cls).__new__(cls)
            return object.__new__(cls)
        return B()

    def __init__(self, a):
        print("INIT", a)

if __name__ == '__main__':
    # __new__ 静态方法创建实例，再把返回值实例对象传给__init__第一个参数
    # 返回实例：super(A, cls).__new__(cls)
    a1 = A(5)  # NEW 5 / B INIT
    a1.fn()  # B fn
    a2 = A(20)  # NEW 20 / INIT 20
    a2.fn()  # A fn
