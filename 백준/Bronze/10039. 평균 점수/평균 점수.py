sum_n = 0

for _ in range(5):
    num = int(input())
    if num < 40:
        sum_n += 40
    else:
        sum_n += num

print(sum_n//5)