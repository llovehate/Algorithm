import sys

for line in sys.stdin.read().splitlines():
    A, B = map(int, line.split())
    print(A + B)