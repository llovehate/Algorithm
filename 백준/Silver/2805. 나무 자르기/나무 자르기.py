import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = max(lst)
result = 0

while start <= end:
    mid = (start + end) // 2
    total = sum(h - mid for h in lst if h > mid)

    if total >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
