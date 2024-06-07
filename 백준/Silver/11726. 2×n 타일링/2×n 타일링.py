N = int(input())
dp = [0, 1, 2, 3, 5]
if N >= 5:
    for i in range(5, N+1):
        val = dp[i-1] + dp[i-2]
        dp.append(val)

print(dp[N] % 10007)