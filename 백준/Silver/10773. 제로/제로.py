K = int(input())

lst = []

for i in range(K):
    num = int(input())
    if num != 0:
        lst.append(num)
    else:
        lst.pop()

if lst:
    print(sum(lst))
else:
    print(0)