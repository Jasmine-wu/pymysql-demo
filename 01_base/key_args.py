a = "tom"
age = 10
# print("this is %s, age is %d"%(a,age))

# format
# print("this is {}, age is {}".format(a, age))
# print("this is {1}, age is {0}, {1} is great".format(age, a))

# dic,list

list1 = ["1", 2, "3", "4"]
# print(*list1)

dic1 = {"key1": "vaule1", "key2": "vaule2", "key3": "vaule3", "key4": "vaule4"}
print("the {1} ".format(*list1))
print("the vaule is value2:{key2},value3:{key3}".format(**dic1))
