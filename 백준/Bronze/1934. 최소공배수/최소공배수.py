import math

T = int(input())

for tc in range(T):
    A, B = map(int, input().split())
    gcd_num = math.gcd(A, B)
    lcm_num = (A * B) // gcd_num
    print(lcm_num)