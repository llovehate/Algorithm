N, M = map(int, input().split())

max_num = 1
divisor = 2

while divisor <= min(N, M):
    if N % divisor == 0 and M % divisor == 0:
        N //= divisor
        M //= divisor
        max_num *= divisor

    else:
        divisor += 1

print(max_num)
print(max_num * N * M)