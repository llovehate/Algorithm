import sys

input = sys.stdin.readline
n, t = map(int, input().split())
lst = list(map(int, input().split()))

prefix = sorted(lst[:t])
result = prefix + lst[t:]

print(" ".join(map(str, result)))