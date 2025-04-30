from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
q = deque()
for _ in range(N):
    word = input().split()
    if word[0] == 'push':
        q.append(int(word[1]))
    elif word[0] == 'pop':
        print(q.popleft() if q else -1)
    elif word[0] == 'size':
        print(len(q))
    elif word[0] == 'empty':
        print(0 if q else 1)
    elif word[0] == 'front':
        print(q[0] if q else -1)
    elif word[0] == 'back':
        print(q[-1] if q else -1)