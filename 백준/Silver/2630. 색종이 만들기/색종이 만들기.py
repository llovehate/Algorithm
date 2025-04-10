import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]

white = 0
blue = 0

def divide(x, y, n):
    global white
    global blue

    color = arr[x][y]
    same = True
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != color:
                same = False
                break
        if not same:
            break

    if same:
        if color == 0:
            white += 1
        else:
            blue += 1
    else:
        half = n // 2
        divide(x, y, half)
        divide(x, y + half, half)
        divide(x + half, y, half)
        divide(x + half, y + half, half)

divide(0, 0, N)
print(white)
print(blue)