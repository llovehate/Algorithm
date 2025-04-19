import heapq
import sys

N = int(input())
heap = []
input = sys.stdin.readline

for _ in range(N):
    x = int(input())
    if x == 0 and heap:
        min_v = heapq.heappop(heap)
        print(-min_v)
    elif x == 0 and not heap:
        print(0)
    else:
        heapq.heappush(heap, -x)