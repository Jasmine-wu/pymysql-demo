import inspect


def a():
    print("======stack",inspect.stack()[0].code_context)

    print("======stack",inspect.stack()[0].function)
    print("======stack",inspect.stack()[1].function)
    print("======stack",inspect.stack()[2].function)



# def b():
#     print("call b")
#
#
def test_stack():
    a()
