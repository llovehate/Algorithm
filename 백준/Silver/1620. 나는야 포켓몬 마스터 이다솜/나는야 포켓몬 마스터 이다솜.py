N, M = map(int, input().split())

name_to_num = {}
num_to_name = {}

for i in range(1, N + 1):
    pokemon = input()
    name_to_num[pokemon] = i
    num_to_name[i] = pokemon

for j in range(M):
    word = input()
    if word.isdigit():
        print(num_to_name[int(word)])
    else:
        print(name_to_num[word])