T = int(input())

for tc in range(T):
    E, V = map(int, input().split())
    print(V - E + 2)