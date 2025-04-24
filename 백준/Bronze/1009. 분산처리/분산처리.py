T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    exp = b % 4 if b % 4 != 0 else 4
    data = a ** exp
    print(10 if data % 10 == 0 else data % 10)