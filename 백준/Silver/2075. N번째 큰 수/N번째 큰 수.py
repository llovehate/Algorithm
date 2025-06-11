import sys
import heapq

input = sys.stdin.readline
N = int(input().split()[0])

min_heap = []

for i in range(N):
    lst = list(map(int, input().split()))
    for num in lst:
        if len(min_heap) < N:
            heapq.heappush(min_heap, num)
        else:
            if num > min_heap[0]:
                heapq.heappushpop(min_heap, num)

print(min_heap[0])