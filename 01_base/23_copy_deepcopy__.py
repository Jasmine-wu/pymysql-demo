import copy

# list dict set truple
# 可变对象和不可变对象
#  里面的值能不能直接被修改

# 能： dict,list, 值被修改，即使被赋值给另一个变量，变量地址也没变
# 不能：tuple ,set

l1 = [1, '2', 3, 4]

dict1 = {'key1': 1, 'key2': 2}

# 元组就是一个列表，只是元组只能查看，不能修改（增、删、改）
tuple1 = (1, "2", 3, 4)

# 集合：一个无序的不重复元素的序列（元素不能是可变类型）
set1 = {1, '2', 3, '4'}
set2 = set()

print(type(tuple1))
print(type(l1))

# 列表可修改
l1[2] = "333"
print(l1)

# 元组不可修改
# set1[2] ="333"
# print(set1)

# 元组不可修改
# tuple1[2] ="333"
# print(tuple1)

# ===========================
# 可变对象地址的变化(重点)

# 可变对象
#  a=b,对b值进行修改，a地址不变，b地址也不变，a，b指向同地址

l2 = l1
print(id(l1))
print(id(l2))
l1[2] = "333"
print(id(l1))
print(id(l2))
print(l1)
print(l2)

# 不可变对象
# a=b ,对b值进行修改,a值不会变，a.b指向地址不同
set3 = set1
print(id(set1))
print(id(set3))
set1 = {3, 5, 'dddd', 4}
print(id(set1))
print(id(set3))

print(set1)
print(set3)

# ====================================
# 可变对象作为参数传入时，在函数中对其本身进行修改，是会影响到全局中的这个变量值的

# 函数默认参数一定要设定为可变参数
# 浅拷贝：拷贝了最外围的对象本身，内部的元素都只是拷贝了一个引用而已
# 和浅拷贝对应，深拷贝拷贝了对象的所有元素，包括多层嵌套的元素，。深拷贝出来的对象是一个全新的对象，不再与原来的对象有任何关联。

# 不可变对象的深/浅拷贝=》不管深/浅，都是值相等，地址也相等
a = 10
b = copy.copy(a)
print(id(a))
print(a)
print(id(b))
print(b)

a = 10
b = copy.deepcopy(a)
print(id(a))
print(a)
print(id(b))
print(b)

# 可变对象的深/浅拷贝=》不管是深宝贝还是浅拷贝，都是值相等，地址不同
l5 = [1, 2, 3]
l6 = copy.copy(l5)
print(id(l5))
print(l5)
print(id(l6))
print(l6)

l7 = copy.deepcopy(l5)
print(id(l5))
print(l5)
print(id(l7))
print(l7)


# ===============================
# 参数传递：python函数参数传递是值传递还是引用传递？
# 这要分传递的参数是可变参数还是不可变参数：

# 函数参数如果是可变参数，就是引用传递
def update(a: list):
    a.append("add")


a = [1, 2, 3]
print("*" * 20)
print(a)
update(a)
print(a)


# 函数参数如果是不可变参数，就是值传递
def add(c):
    c += 1


c = 10
print(c)
add(c)
print(c)


# ================面试题====
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print("list1 = %s" % list1) # 10,a
print("list2 = %s" % list2) # 123
print("list3 = %s" % list3) # 10,a


# 改进：==========================
# 希望输出的是 [10] [123] [a]
def extendList(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123, [])
list3 = extendList('a')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)

