import sys

input = sys.stdin.readline
N = int(input())
stack = []

for _ in range(N):
    word = input()
    if word[0] == '1':
        one, two = map(int, word.split())
    else:
        one = int(word)

    if one == 1:
        stack.append(two)
    elif one == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif one == 3:
        print(len(stack))
    elif one == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif one == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)