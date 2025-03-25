import math

N = int(input())
num = str(math.factorial(N))
cnt = 0

for i in num[::-1]:
    if i == '0':
        cnt += 1
    else:
        break

print(cnt)