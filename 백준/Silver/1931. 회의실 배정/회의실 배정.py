N = int(input())
lst = []
cnt = 1

for i in range(N):
    lst.append(list(map(int, input().split())))

lst.sort(key=lambda x: (x[1], x[0]))

ex_room = lst[0]
for j in lst[1:]:
    if ex_room[1] <= j[0]:
        cnt += 1
        ex_room = j


print(cnt)