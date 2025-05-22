N = int(input())
my_str = input()
cnt = 0


def train(idx):
    global cnt

    if my_str[idx-1] == '[':
        cnt += 1
    elif my_str[idx-1] == '5':
        if my_str[idx] == '5':
            cnt += 2
        else:
            cnt += 1
    elif my_str[idx-1] == '2':
        if my_str[idx] == '2':
            cnt += 2
        else:
            cnt += 1
    else:
        if my_str[idx] != '[':
            cnt += 1


for i in range(1, N):
    train(i)

print(cnt)