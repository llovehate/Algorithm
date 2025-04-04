N = int(input())
cnt = 0

for i in range(N):
    word = input()
    lst = []
    result = []
    flag = True

    for j in range(len(word)):
        if word[j] not in lst:
            lst.append(word[j])
        elif word[j] in lst and word[j-1] == word[j]:
            pass
        else:
            flag = False
            break
    if flag:
       cnt += 1

print(cnt)