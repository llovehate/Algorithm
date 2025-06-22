N = int(input())
rm_sum = []
min_v = 9999999

for _ in range(N):
    A, B, C = map(int, input().split())
    rm_sum.append(A + B + C)

for i in rm_sum:
    if i >= 512 and i < min_v:
        min_v = i

if min_v != 9999999:
    print(min_v)
else:
    print(-1)