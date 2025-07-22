import sys
input = sys.stdin.readline

for _ in range(3):
    N = int(input())
    sum_v = 0
    for i in range(N):
        num = int(input())
        sum_v += num
    if sum_v == 0:
        print(0)
    else:
        print('+' if sum_v > 0 else '-')