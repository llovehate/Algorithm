N = int(input())
lst = list(map(int, input().split()))
T, P = map(int, input().split())

t_result = 0

for i in lst:
    ans = i // T
    if ans == 0 and i % T != 0:
        ans = 1
    elif i % T != 0:
        ans += 1
    t_result += ans

pen_result = N // P
pen_single = N % P

print(t_result)
print(pen_result, pen_single)