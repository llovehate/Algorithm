import sys

input = sys.stdin.readline
N, M = map(int, input().split())
S = set(input() for _ in range(N))
cnt = 0

for _ in range(M):
    my_str = input()
    if my_str in S:
        cnt += 1

print(cnt)