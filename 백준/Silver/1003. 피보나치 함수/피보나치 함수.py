T = int(input())
for tc in range(T):
    N = int(input())
    dp_zero = [1, 0, 1, 1]
    dp_one = [0, 1, 1, 2]
    if N >= 4:
        for i in range(4, N+1):
            val_zero = dp_zero[i-1] + dp_zero[i-2]
            val_one = dp_one[i-1] + dp_one[i-2]
            dp_zero.append(val_zero)
            dp_one.append(val_one)
    print(dp_zero[N], dp_one[N])