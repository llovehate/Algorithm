import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

prefix_sum = [0]
for num in lst:
    prefix_sum.append(prefix_sum[-1] + num)

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])
