N = input()
cnt = 0
num = N
new_num = 100

while int(N) != new_num:
    if int(num) < 10:
        add = str(num)
    else:
        add = str(int(num[1]) + int(num[0]))
    new_num = int(num[-1] + add[-1])
    num = num[-1] + add[-1]
    cnt += 1

print(cnt)