# python的内存管理机制

# 内存的分配： 内存池

# 内存的销毁： 垃圾回收机制，以引用计数sys.getrefcount()为主，标记-清除和分代回收为辅

# 什么情况引用计数+1：新创建，被其他人引用
# -1：引用它的便变量名被显式del销毁，被从容器里删除

# 标记-清除：解决循环引用问题，循环引用只有在容器对象才产生

import sys
import gc
# a=[1,2]
# print(sys.getrefcount(a))
# b=a
# print(sys.getrefcount(a))
#
# del b  ## 删除b的引用
# print(sys.getrefcount(a))
# #
# c=list()
# c.append(a) ## 加入到容器中
# print(sys.getrefcount(a))
# #
# del c  ## 删除容器，引用-1
# print(sys.getrefcount(a))
# #
#
#
# print("#"*50)
# b=a
#
# print(sys.getrefcount(a))
#
# a=[3,4]  ##重新赋值
# print(sys.getrefcount(a))



#  循环引用
print("循环引用"+"*"*50)
a=[1,2]
b=[3,4]
print(sys.getrefcount(a))

print(sys.getrefcount(b))

a.append(b)
print(sys.getrefcount(b))

b.append(a)
print(sys.getrefcount(a))

del a
del b

print(gc.get_threshold())

