S = int(input())

num = 1
ans = 0
while True:
    if num % 2 == 0:
        ans = (num + 1) * (num // 2)
    else:
        ans = (num + 1) * (num // 2) + (num // 2 + 1)

    if ans > S:
        num -= 1
        break
    elif ans == S:
        break
    num += 1

print(num)