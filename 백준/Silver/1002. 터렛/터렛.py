T = int(input())

for tc in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dx = x1 - x2
    dy = y1 - y2
    # 두 원 사이의 거리 제곱 (루트로 비교할 경우 부동소수점 차이가 날 수 있으므로)
    d_sq = dx * dx + dy * dy

    sum_r = r1 + r2
    diff_r = abs(r1 - r2)

    # 두 원의 반지름의 합의 제곱
    sum_r_sq = sum_r * sum_r
    # 두 원의 반지름의 차의 제곱
    diff_r_sq = diff_r * diff_r

    # 두 원의 중심이 같음
    if d_sq == 0:
        # 두 원의 반지름이 같음
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        # 원이 만나지 않음
        if d_sq > sum_r_sq:
            print(0)
        # 외접
        elif d_sq == sum_r_sq:
            print(1)
        # 2점에서 만남
        elif diff_r_sq < d_sq < sum_r_sq:
            print(2)
        # 내접
        elif d_sq == diff_r_sq:
            print(1)
        # 작은 원이 큰 원 안에 들어있음
        elif d_sq < diff_r_sq:
            print(0)