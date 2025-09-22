N = int(input())

for i in range(N):
    print("*" * (i+1) + " " * (2 * N - 2 - 2 * i) + "*" * (i+1))

for j in range(N-2, -1, -1):
    print("*" * (j+1) + " " * (2 * N - 2 - 2 * j) + "*" * (j+1))