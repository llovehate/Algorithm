import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
adj = [[] for _ in range(N+1)]
parent = [-1] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def dfs(cur, p):
    # 현재 노드의 부모를 설정
    parent[cur] = p
    for nxt in adj[cur]:
        # 다음 노드를 아직 방문하지 않았다면
        if parent[nxt] == -1:
            # 다음 노드의 부모를 현재 노드로 설정
            dfs(nxt, cur)

# 루트 노드인 1번 노드의 부모를 0으로 설정
dfs(1, 0)

for i in range(2, N+1):
    print(parent[i])