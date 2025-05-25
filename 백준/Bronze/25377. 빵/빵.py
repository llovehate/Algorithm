import sys

input = sys.stdin.readline
N = int(input())
result = 9999

for _ in range(N):
    A, B = map(int, input().split())
    if A <= B:
        result = min(result, B)

print(result if result != 9999 else -1)