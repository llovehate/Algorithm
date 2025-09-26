N = int(input())
lst = []
result = ""

for i in range(N):
    lst.append(input())

for j in range(len(lst[0])):
    alpha = []
    flag = True
    for k in range(N):
        alpha.append(lst[k][j])
    for l in range(1, N):
        if alpha[l-1] != alpha[l]:
            flag = False
            break
    if flag:
        result += alpha[0]
    else:
        result += "?"

print(result)