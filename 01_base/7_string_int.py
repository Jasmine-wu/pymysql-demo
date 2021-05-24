import re
# 数字转字符串
a = 133
print(str(a))
print('%d'%a)

# 字符串转数字
print(int("133"))

totalCount = '100abc'
# \D 匹配非数字用""替代
totalCount = re.sub("\D", "", totalCount)
print(totalCount)
print(type(totalCount))
