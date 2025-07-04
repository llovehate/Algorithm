import sys
import math
input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]
gaps = []
cnt = 0

for i in range(1, N):
    tree_distance = lst[i] - lst[i-1]
    gaps.append(tree_distance)

gcd = gaps[0]
for gap in gaps[1:]:
    gcd = math.gcd(gcd, gap)

for gap in gaps:
    cnt += (gap // gcd) - 1

print(cnt)