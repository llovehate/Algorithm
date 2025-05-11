import sys

input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
x = int(input())

seen = set()
cnt = 0

for i in lst:
    if x - i in seen:
        cnt += 1
    seen.add(i)

print(cnt)