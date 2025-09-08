name = set()
name_cnt = []
result = []

N = int(input())
for _ in range(N):
    name_first = input()[0]
    name.add(name_first)
    name_cnt.append(name_first)

for i in name:
    cnt = 0
    for j in name_cnt:
        if i == j:
            cnt += 1
    if cnt >= 5:
        result.append(i)

if result:
    result.sort()
    print("".join(result))
else:
    print("PREDAJA")