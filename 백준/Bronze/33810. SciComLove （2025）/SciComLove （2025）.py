S = input()

my_str = 'SciComLove'
cnt = 0

for i in range(10):
    if S[i] != my_str[i]:
        cnt += 1

print(cnt)