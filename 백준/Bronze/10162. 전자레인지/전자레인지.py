T = int(input())
A = 0
B = 0
C = 0

if T >= 300:
    A = T // 300
    T = T - (A * 300)
if T >= 60:
    B = T // 60
    T = T - (B * 60)
if T >= 10:
    C = T // 10
    T = T - (C * 10)

print(f'{A} {B} {C}' if not T else -1)