N, S = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0

def backtracking(idx, c_sum):
    global cnt

    if idx == N:
        if c_sum == S:
            cnt += 1
        return

    backtracking(idx + 1, c_sum + lst[idx])
    backtracking(idx + 1, c_sum)

backtracking(0, 0)

if S == 0:
    cnt -= 1

print(cnt)