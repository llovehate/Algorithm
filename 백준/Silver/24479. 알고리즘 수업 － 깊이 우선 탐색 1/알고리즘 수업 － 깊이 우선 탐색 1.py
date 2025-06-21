import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
adj = [[] for _ in range(N)]
visited = [False] * N
result = [0] * N
num = 1

for i in range(M):
    u, v = map(int, input().split())
    adj[u-1].append(v)
    adj[v-1].append(u)

for j in range(N):
    adj[j].sort()

def dfs(n):
    global num
    visited[n-1] = True
    result[n-1] = num
    num += 1

    for i in adj[n-1]:
        if not visited[i-1]:
            dfs(i)

dfs(R)
print("\n".join(map(str, result)))