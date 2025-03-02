while True:
    lst = list(map(int, input().split()))
    lst.sort()
    A = lst[0]
    B = lst[1]
    C = lst[2]

    if A == 0:
        break

    if A ** 2 + B ** 2 == C ** 2:
        print("right")
    else:
        print("wrong")