from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt = 0


def bfs(x, y):
    global cnt
    q = deque([(x, y)])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            ni = x + di[i]
            nj = y + dj[i]
            if 0 <= ni < N and 0 <= nj < M:
                if arr[ni][nj] != 'X' and visited[ni][nj] != 1:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                    if arr[ni][nj] == 'P':
                        cnt += 1


for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            bfs(i, j)

print(cnt if cnt > 0 else "TT")