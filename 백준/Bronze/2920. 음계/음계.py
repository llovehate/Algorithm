lst = list(map(int, input().split()))

flag = 0

if lst[0] == 1:
    for i in range(1, 7):
        if lst[i] == lst[i-1] + 1:
            pass
        else:
            print("mixed")
            flag = 1
            break
    if flag == 0:
        print("ascending")

elif lst[0] == 8:
    for i in range(1, 7):
        if lst[i] == lst[i-1] - 1:
            pass
        else:
            print("mixed")
            flag = 1
            break
    if flag == 0:
        print("descending")
else:
    print("mixed")