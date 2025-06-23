N = int(input())
start = 1
end = 1
total = 1
cnt = 0

while start <= N:
    if total == N:
        cnt += 1
        total -= start
        start += 1
    elif total < N:
        end += 1
        total += end
    elif total > N:
        total -= start
        start += 1

print(cnt)