T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    rare = list(map(int, input().split()))
    numbers = [i for i in range(1, N + 1)]
    target = numbers[M]
    target_rare = rare[M]
    cnt = 0

    while numbers:
        num = rare[0]
        if num < max(rare):
            num_real = numbers.pop(0)
            num_rare = rare.pop(0)
            numbers.append(num_real)
            rare.append(num_rare)
        else:
            target_num = numbers.pop(0)
            rare.pop(0)
            cnt += 1
            if target_num == target:
                break

    print(cnt)