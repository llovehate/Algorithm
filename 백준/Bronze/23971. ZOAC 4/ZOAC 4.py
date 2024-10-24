H, W, N, M = map(int, input().split())

row_people = 0
row = 1
col = 1
col_num = 0

while True:
    row_people += 1
    row += M + 1
    if row > W:
        break

while True:
    col_num += 1
    col += N + 1
    if col > H:
        break

result = row_people * col_num

print(result)