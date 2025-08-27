color = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

num = ''
multi = [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]
for i in range(3):
    word = input()
    if i == 2:
        num = int(num) * multi[color[word]]
    else:
        num += str(color[word])

print(num)