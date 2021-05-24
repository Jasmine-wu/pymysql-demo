# l=[1,2,3,4,5,6,7,8] 数据不重复，target=6，快速找出数组中两个元素之和等于target 的数组下标

def get_num(l, target):
    #  去重
    set1 = set(l)
    result = []

    for a in set1:
        b = target - a
        if a < b < target and b in set1:  # 在集合中查找,为避免重复，判断a为较小的那个值（0，4）（4，0）
            result.append((l.index(a), l.index(b)))  # 列表index取下标的操作为O(1)
    return result



# [(0, 4), (1, 3)]
if __name__ == '__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8]
    # print(get_num(l, 6))
    print(result(l, 6))


