import sys

input = sys.stdin.readline
N, M = map(int, input().split())
memo = {}

for _ in range(N):
    url, password = input().split()
    memo[url] = password

for _ in range(M):
    url = input().strip()
    print(memo[url])