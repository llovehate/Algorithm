N, M = map(int, input().split())

visited = [False] * (N + 1)
result = []

def backtracking():
    if len(result) == M:
        print(" ".join(map(str, result)))
        return
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            backtracking()
            result.pop()
            visited[i] = False

backtracking()