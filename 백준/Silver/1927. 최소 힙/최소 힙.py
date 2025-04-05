import sys
import heapq

input = sys.stdin.readline
heap = []
N = int(input())

for i in range(N):
    num = int(input())
    if num == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
           print(0)
    else:
        heapq.heappush(heap, num)