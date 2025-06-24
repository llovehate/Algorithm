N = int(input())
gongbaekfront = N - 1
gongbaekmiddle = 1

for i in range(1, N + 1):
    if i == 1:
        print((" " * gongbaekfront) + "*")
        gongbaekfront -= 1
    elif i == N:
        print("*" * (N * 2 - 1))
    else:
        print((" " * gongbaekfront) + "*" + (" " * gongbaekmiddle) + "*")
        gongbaekfront -= 1
        gongbaekmiddle += 2