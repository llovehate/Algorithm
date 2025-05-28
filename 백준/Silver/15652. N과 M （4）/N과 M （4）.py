N, M = map(int, input().split())
result = []


def backtrack(n):
    if len(result) == M:
        print(*result)
        return

    for i in range(n, N+1):
        result.append(i)
        backtrack(i)
        result.pop()


backtrack(1)