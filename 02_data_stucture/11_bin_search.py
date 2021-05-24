#二分查找需要序列首先有序。
# 思想是先用序列中间数和目标值对比，如果目标值小，则从前半部分（小于中间数）重复此查找，否则从后半部分重复此查找。
# 返回的是下标
def bin_search(l,n):
    # 找到最后都没找到或者一开始列表为空时候

    if len(l) == 0:
        return False

    mid = len(l) // 2

    if l[mid] == n:
        return True
    if l[mid] > n:
        return bin_search(l[:mid], n)
    else:
        return bin_search(l[mid+1:], n)


#======== 面试题=============
def p1(x, y):
    print("%s/%s = %s" % (x, y, x / y))

def p2(x, y):
    print("%s//%s = %s" % (x, y, x // y))

p1(5, 2) # 2。5
p1(5., 2) # 2 .5
p2(5, 2) # 2
p2(5., 2.) # 2.0

if __name__ == '__main__':
    # a = 10
    # b = 6
    # # 向下取整
    # print("a//b=", a//b)
    # print("a/b=", a/b)

    # print(bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))
    print(bin_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 99))