import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
lst = []

count = [0] * 8001
total = 0

for _ in range(N):
    num = int(input())
    lst.append(num)
    count[num + 4000] += 1
    total += num

print(round(total / N))

lst.sort()
print(lst[N // 2])

max_freq = max(count)
modes = []

for i in range(len(count)):
    if count[i] == max_freq:
        modes.append(i - 4000)

modes.sort()
print(modes[1] if len(modes) > 1 else modes[0])

print(max(lst) - min(lst))