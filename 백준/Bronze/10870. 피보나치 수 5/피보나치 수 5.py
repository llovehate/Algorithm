N = int(input())

d = [0, 1]
if N >= 2:
    for i in range(2, N + 1):
        d.append(d[i-1] + d[i-2])

print(d[N])