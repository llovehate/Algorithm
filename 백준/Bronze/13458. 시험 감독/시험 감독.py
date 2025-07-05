N = int(input())
lst = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0

for i in lst:
    if i - B > 0:
        if (i - B) % C:
            cnt += ((i - B) // C) + 2
        else:
            cnt += ((i - B) // C) + 1
    else:
        cnt += 1

print(cnt)