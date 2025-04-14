L, P = map(int, input().split())
lst = list(map(int, input().split()))

people = L * P
for i in lst:
    print(i - people, end=" ")