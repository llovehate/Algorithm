N = int(input())
result = []

if N != 1:
    divide = 2
    while N != 1:
        if N % divide == 0:
            N //= divide
            result.append(divide)
        else:
            divide += 1

print("\n".join(map(str, result)))