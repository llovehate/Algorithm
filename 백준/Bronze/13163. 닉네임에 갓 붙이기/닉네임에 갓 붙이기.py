N = int(input())

for _ in range(N):
    name = list(input().split())
    name[0] = 'god'
    print(''.join(name))