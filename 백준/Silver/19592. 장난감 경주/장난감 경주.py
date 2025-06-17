T = int(input())

for tc in range(T):
    result = []
    N, X, Y = map(int, input().split())
    velocity = list(map(int, input().split()))

    for i in range(N - 1):
        result.append(X / velocity[i])

    def win(booster):
        time = ((X - booster) / velocity[N-1]) + 1
        return time < min(result)

    if (X / velocity[N-1]) < min(result):
        print(0)
        continue

    if not win(Y):
        print(-1)
        continue

    left, right = 1, Y
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if win(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    print(ans)