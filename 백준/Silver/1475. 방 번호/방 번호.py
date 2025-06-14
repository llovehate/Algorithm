N = input()
lst = [0] * 10

for i in N:
    lst[int(i)] += 1

if max(lst) == lst[6] or max(lst) == lst[9]:
    num = (lst[6] + lst[9] + 1) // 2
    lst[6] = 0
    lst[9] = 0
    print(max(num, max(lst)))
else:
    print(max(lst))