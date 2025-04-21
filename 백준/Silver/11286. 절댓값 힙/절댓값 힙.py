import sys
import heapq

input = sys.stdin.readline
heap = []
N = int(input())

for _ in range(N):
    word = int(input())
    if word != 0:
        heapq.heappush(heap, (abs(word), word))
    elif heap and word == 0:
        ans = heapq.heappop(heap)[1]
        print(ans)
    else:
        print(0)