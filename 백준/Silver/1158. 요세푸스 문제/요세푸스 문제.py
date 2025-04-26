from collections import deque

N, K = map(int, input().split())
lst = list(range(1, N+1))
idx = 0
result = []

while lst:
    idx = (idx + K - 1) % len(lst)

    num = lst.pop(idx)
    result.append(num)

print('<', end='')
for i in range(N):
    if i == N-1:
        print(result[i], end='')
    else:
        print(result[i], end=', ')
print('>')