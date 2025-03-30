import sys

N, M = map(int, input().split())

heard = set(sys.stdin.readline().strip() for _ in range(N))
looked = set(sys.stdin.readline().strip() for _ in range(M))

result = sorted(heard & looked)

print(len(result))
for j in result:
    print(j)