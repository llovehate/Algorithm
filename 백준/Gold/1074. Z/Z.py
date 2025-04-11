def visit(x, y, n):
    global cnt
    if n == 0:
        return

    half = 2 ** (n-1)

    if r < x + half and c < y + half:
        visit(x, y, n - 1)
    elif r < x + half and c >= y + half:
        cnt += half * half
        visit(x, y + half, n - 1)
    elif r >= x + half and c < y + half:
        cnt += 2 * (half * half)
        visit(x + half, y, n - 1)
    elif r >= x + half and c >= y + half:
        cnt += 3 * (half * half)
        visit(x + half, y + half, n - 1)


N, r, c = map(int, input().split())
cnt = 0
visit(0, 0, N)
print(cnt)