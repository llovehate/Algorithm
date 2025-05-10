N, M = map(int, input().split())
result = []
visited = [False] * (N + 1)

def backtracking(start):
    if len(result) == M:
        print(" ".join(map(str, result)))
        return

    for i in range(start, N+1):
        if not visited[i]:
            result.append(i)
            visited[i] = True
            backtracking(i+1)
            result.pop()
            visited[i] = False

backtracking(1)