T = int(input())
for tc in range(T):
    N = int(input())
    dp = [0, 1, 2, 4, 7, 13]
    if N >= 6:
        for i in range(6, N + 1):
            val = dp[i-3] + dp[i-2] + dp[i-1]
            dp.append(val)
    print(dp[N])