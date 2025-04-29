from collections import defaultdict

T = int(input())

for _ in range(T):
    n = int(input())
    clothes = defaultdict(int)

    for _ in range(n):
        name, kind = input().split()
        clothes[kind] += 1

    ans = 1
    for i in clothes.values():
        ans *= (i + 1)

    print(ans - 1)