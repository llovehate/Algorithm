import sys

def custom_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

N = int(input())

if N == 0:
    print(0)
else:
    lst = [int(sys.stdin.readline()) for _ in range(N)]
    lst.sort()
    except_num = custom_round(N * 0.15)
    result = 0

    for i in range(except_num, N-except_num):
        result += lst[i]

    result = custom_round(result / (N - 2 * except_num))

    print(result)