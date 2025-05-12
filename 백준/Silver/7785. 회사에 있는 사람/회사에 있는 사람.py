import sys

input = sys.stdin.readline
n = int(input())
log = set()

for _ in range(n):
    name, now = input().split()
    if now == 'enter':
        log.add(name)
    else:
        log.remove(name)

for name in sorted(log, reverse=True):
    print(name)