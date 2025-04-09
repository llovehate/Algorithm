import sys

input = sys.stdin.readline
output = sys.stdout.write

M = int(input())
S = set()

for _ in range(M):
    task = list(input().split())
    word = task[0]
    if len(task) > 1:
        num = int(task[1])
    if word == 'add':
        S.add(num)
    elif word == 'remove':
        S.discard(num)
    elif word == 'check':
        output('1\n' if num in S else '0\n')
    elif word == 'toggle':
        if num in S:
            S.discard(num)
        else:
            S.add(num)
    elif word == 'all':
        S.clear()
        S.update(range(1, 21))
    elif word == 'empty':
        S.clear()