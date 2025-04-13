while True:
    my_str = input()
    cnt = 0

    if my_str == '#':
        break

    for i in my_str:
        if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
            cnt += 1
    print(cnt)