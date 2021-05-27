# from threading import Thread
# import time
# lqz = 10
# def task(arg):
#     global lqz
#     lqz = arg
#     time.sleep(2)
#     print(lqz) # 打印了10个9
#
# for i in range(10):
#     t = Thread(target=task,args=(i,))
#     t.start()

# 改进====================用local
# from threading import Thread
# from threading import local
# import time
# from threading import get_ident
#
# # 特殊的对象
# lqz = local()
# {'线程id1'：{value:1}},{'线程id2':{value:2}}
#
#
# def task(arg):
#     # 对象.val = 1/2/3/4/5
#     lqz.value = arg
#     time.sleep(2)
#     print(lqz.value) # 打印0-9
#
# for i in range(10):
#     t = Thread(target=task, args=(i,))
#     t.start()

# =======================不用local，自己实现一个local
# from threading import get_ident,Thread
# import time
# storage = {}
# def set(k,v):
#     # 线程id号：get_ident()
#     ident = get_ident()
#     if ident in storage:
#         storage[ident][k] = v
#     else:
#         storage[ident] = {k:v}
#
# def get(k):
#     ident = get_ident()
#     return storage[ident][k]
#
# def task(arg):
#     set('val',arg)
#     v = get('val')
#     print(v)
#
# for i in range(10):
#     t = Thread(target=task,args=(i,))
#     t.start()

# ================ 改进：写成面向对象版本
from threading import get_ident, Thread
import time

#
# class Local(object):
#     storage = {}
#
#     def set(self, k, v):
#         ident = get_ident()
#         if ident in Local.storage:
#             Local.storage[ident][k] = v
#         else:
#             Local.storage[ident] = {k: v}
#
#     def get(self, k):
#         ident = get_ident()
#         return Local.storage[ident][k]
#
#
# obj = Local()
#
#
# def task(arg):
#     obj.set('val', arg)
#     v = obj.get('val')
#     print(v)
#
#
# for i in range(10):
#     t = Thread(target=task, args=(i,))
#     t.start()

# ==============  该进：通过__setattr__，__getattr__实现
from threading import get_ident, Thread
import time
class Local(object):
    storage = {}

    def __setattr__(self, k, v):
        ident = get_ident()
        if ident in Local.storage:
            Local.storage[ident][k] = v
        else:
            Local.storage[ident] = {k: v}

    def __getattr__(self, k):
        ident = get_ident()
        return Local.storage[ident][k]

obj = Local()

def task(arg):
    # 对象.会触发__setattr__和__getattr__方法
    obj.val = arg
    print(obj.val)

for i in range(10):
    t = Thread(target=task, args=(i,))
    t.start()
