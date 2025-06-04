A, B, C = map(int, input().split())

def mod_pow(a, b, c):
    # 더 이상 나눌 수 없을 때
    if b == 1:
        return a % c

    # b 값을 나누며 half 구하기 위한 재귀 호출
    half = mod_pow(a, b // 2, c)
    # b가 짝수일 때
    if b % 2 == 0:
        return (half * half) % c
    # b가 홀수일 때
    else:
        return (half * half) * a % c

print(mod_pow(A, B, C))