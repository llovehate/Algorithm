import sys

N = int(input())
lst = []

for i in range(N):
    age, name = sys.stdin.readline().strip().split()
    lst.append((int(age), name))

lst.sort(key=lambda x: x[0])

for age, name in lst:
    print(age, name)