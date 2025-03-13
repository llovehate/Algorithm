lst = list(map(int, input().split()))

ans = 0

for i in range(5):
    ans += (lst[i] ** 2)

print(ans % 10)