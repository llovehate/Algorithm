import sys

while True:
    my_str = sys.stdin.readline().rstrip()
    if my_str == ".":
        break

    stack = []
    flag = True

    for i in my_str:
        if i == '[' or i == '(':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] != '(':
                flag = False
                break
            else:
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] != '[':
                flag = False
                break
            else:
                stack.pop()

    if flag and not stack:
        print('yes')
    else:
        print('no')