lst = [list(input()) for _ in range(8)]
cnt = 0

for i in range(8):
    for j in range(8):
        if lst[i][j] == 'F':
            if i % 2 == 0:
                if j % 2 == 0:
                    cnt += 1
            else:
                if j % 2 != 0:
                    cnt += 1

print(cnt)