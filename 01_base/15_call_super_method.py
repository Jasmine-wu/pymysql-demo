#  如何调用父类
class A:
    def show(self):
        print("A show")

class B(A):
    def show(self):
        print("B show")

if __name__ == "__main__":
    b = B()

    b.__class__ = A
    b.show() # A show
    print(b.__class__)