# 【python】不用加减乘除运算实现加法？
# 位运算

def add(a, b):

    while True:
        sum = a ^ b
        carry = (a & b) << 1
        a = sum
        b = carry
        if carry == 0:
            break
    return sum

if __name__ == "__main__":
    print(add(77,88))

