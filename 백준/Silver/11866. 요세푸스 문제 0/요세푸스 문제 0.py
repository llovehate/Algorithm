N, K = map(int, input().split())

lst = []
circle = []

for i in range(1, N + 1):
    circle.append(i)

idx = 0
while circle:
    idx += K - 1
    if idx >= len(circle):
        idx %= len(circle)

    lst.append(circle[idx])
    circle.pop(idx)

print("<", end="")
for num in range(len(lst)):
    if num != len(lst) - 1:
        print(lst[num], end=", ")
    else:
        print(lst[num], end="")
print(">")