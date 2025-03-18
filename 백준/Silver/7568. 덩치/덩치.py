N = int(input())
lst = []
result = []

for i in range(N):
    weight, tall = map(int, input().split())
    lst.append((weight, tall))

for (tall_n, weight_n) in lst:
    ans = 1
    for (tall, weight) in lst:
        if tall_n < tall and weight_n < weight:
            ans += 1
    result.append(ans)

print(*result, end=" ")