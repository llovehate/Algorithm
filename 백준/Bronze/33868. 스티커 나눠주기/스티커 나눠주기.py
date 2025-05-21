N = int(input())
times = []
codes_len = []

for _ in range(N):
    T, B = map(int, input().split())
    times.append(T)
    codes_len.append((B))

print(((max(times) * min(codes_len)) % 7) + 1)