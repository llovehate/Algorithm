for _ in range(3):
    lst = list(map(int, input().split()))
    sum_num = 0

    for i in lst:
        sum_num += i

    if sum_num == 0:
        print("D")
    elif sum_num == 1:
        print("C")
    elif sum_num == 2:
        print("B")
    elif sum_num == 3:
        print("A")
    else:
        print("E")