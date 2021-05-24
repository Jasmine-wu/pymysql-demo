from collections import Counter


# 字符串统计#
def count(content: str):
    l = set(content)
    result = []
    for s in l:
        result.append((s, content.count(s)))
    return result

# 统计重复最多的n个字符#
def max(l: list, n):
    l.sort(key=lambda x: x[1], reverse=True)
    return l[:n]


def test(l: str):
    # 统计
    c = Counter(l)
    print(c.items())
    # 取最大
    print(c.most_common(3))


# 字符串反转：使用反向切片或者reverse实现。
def string_reverse(s):
    return s[::-1]


def string_reverse2(s):
    return "".join(reversed(s))


# 包含数字字母的字符串，仅反转字母
# 将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中
def string_reverse3(s):
    result = []
    l = len(s)
    for i,c in enumerate(s):
        # print(i,c)
        if c.isdigit():
            result.append(c)
        else:
            result.append(s[l-i-1])
        #  简化
        # result.append(c) if c.isdigit() else result.append(a[l - i - 1])
    return "".join(result)


def test2(a):
    l = len(a)
    r = []
    for i, c in enumerate(a):
        r.append(c) if c.isdigit() else r.append(a[l - i - 1])
    print(''.join(r))


if __name__ == '__main__':
    l = "abcdaacddddddddddceeag09l"
    # print(count(l))
    # print(max(count(l),3))
    # test(l)

    # s = "33xxxbbb2"
    # print(string_reverse(s))
    # print(string_reverse2(s))
    # print(string_reverse3(s))
    # test2(s)

    text = "({[({{abc}})][{1}]})2([]){({[]})}[]"
    # print(is_closed(text))
    test(l)


