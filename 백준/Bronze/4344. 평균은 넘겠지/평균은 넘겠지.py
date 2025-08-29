N = int(input())

for _ in range(N):
    lst = list(map(int, input().split()))
    scores = lst[1:]
    scores_avg = sum(scores) / lst[0]
    cnt = 0
    for i in scores:
        if i > scores_avg:
            cnt += 1
    result = round((cnt / lst[0]) * 100, 3)
    print(f"{result:.3f}%")