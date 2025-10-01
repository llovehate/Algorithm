import math

A, I = map(int, input().split())

I = I - 1 + 0.00000001
print(math.ceil(A * I))