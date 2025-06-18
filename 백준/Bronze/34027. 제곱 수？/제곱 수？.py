import math

T = int(input())

for tc in range(T):
    N = int(input())
    if math.sqrt(N).is_integer():
        print(1)
    else:
        print(0)
