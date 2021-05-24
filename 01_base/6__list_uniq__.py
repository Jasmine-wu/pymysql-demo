from collections import Counter
# 两道题
# 列表去重，列出重复的字符，重复的次数
# 字符串去重，列出某字符重复的次数

# ======== list =====================
a = [1, 2, 3, 3, 4, 4]
# 列表去重，找出重复的字符

# 去重，一行代码搞定，但是无法得出重复的字符,以及重复的次数,也无法保证去重的顺序
print(list(set(a)))
la = list(set(a))
#  保证去重后的顺序
la.sort(key=a.index)
print(la)


# 找出所有重复的,显示重复的次数
dic = dict(Counter(a))
# for key,value in dic.items():
#     if value > 1:
#         print(key)
print([key for key, value in dic.items() if value > 1])
print([(key,value) for key, value in dic.items() if value > 1])

# 某字符重复了多少次
print([value for key, value in dic.items() if value > 1 and key==3])

# 不用collection模块手动实现
print('*'*50)
lb = list(set(a))
# result = []
# for item in lb:
#     result.append((item, a.count(item)))
result = {item:a.count(item) for item in lb}
print([(key,value) for key, value in result.items() if value > 1])

# 二维列表排序
result = [(item,a.count(item)) for item in lb]
result.sort(key=lambda x:x[1], reverse=True)
print(result)

# ======== string =====================
l = "abcdaacddddddddddceeag09l"
# set无重无法保证去重后的顺序
print((set(l)))
