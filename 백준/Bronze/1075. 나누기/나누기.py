N = int(input())
F = int(input())

num = N // 100
num = int(str(num)+'00')
number = num // F
result = F * number

while result >= num:
    number -= 1
    result = F * number
result = F * (number + 1)

print(str(result)[-2:])