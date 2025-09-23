N = int(input())
sub = 1000- N
cnt = 0

while sub > 0:
    if sub >= 500:
        cnt += 1
        sub -= 500
    elif sub >= 100:
        cnt += 1
        sub -= 100
    elif sub >= 50:
        cnt += 1
        sub -= 50
    elif sub >= 10:
        cnt += 1
        sub -= 10
    elif sub >= 5:
        cnt += 1
        sub -= 5
    else:
        cnt += 1
        sub -= 1

print(cnt)