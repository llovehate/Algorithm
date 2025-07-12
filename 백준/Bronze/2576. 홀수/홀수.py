numbers = []

for _ in range(7):
    num = int(input())
    if num % 2 != 0:
        numbers.append(num)

if numbers:
    print(sum(numbers))
    print(min(numbers))
else:
    print(-1)