alpha = input()
change = ['c=', 'c-', 'lj', 'nj', 's=', 'z=']
cnt = 0
idx = 0

while True:
    if alpha[idx] != 'd':
        if alpha[idx:idx+2] in change:
            cnt += 1
            idx += 2
        else:
            cnt += 1
            idx += 1
    else:
        if alpha[idx:idx+3] == 'dz=':
            cnt += 1
            idx += 3
        elif alpha[idx:idx+2] == 'd-':
            cnt += 1
            idx += 2
        else:
            cnt += 1
            idx += 1

    if idx == len(alpha):
        break

print(cnt)