S = input()
lst = [0] * 26

for i in S:
    lst[ord(i)-97] += 1

print(*lst)