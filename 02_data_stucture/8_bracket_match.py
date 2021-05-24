
# 括号匹配
def is_close(s):
    stack = []
    bracket = {'}':'{', ']':'[',')':'('}
    for char in s:
        # 如果是反括号
        if char in bracket.values():
            # 正括号入栈
            stack.append(char)
        # 如果是反括号
        elif char in bracket.keys():
            # 如果反括号对应的正括号跟栈顶的元素匹配
            if bracket[char] == stack.pop():
                return True
            else:
                return False
    return True

if __name__ == '__main__':
    text = "{[({{abc}})][{1}]})2([]){({[]})}[]"
    print(is_close(text))
    # print(is_closed(text))

