K, N = map(int, input().split())
lst = [int(input()) for _ in range(K)]

start = 1
end = max(lst)

result = 0

while start <= end:
    mid = (start + end) // 2
    cnt = sum(i // mid for i in lst)

    if cnt >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)