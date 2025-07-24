N = int(input())

for _ in range(N):
    word = input()
    print('yes' if (len(word) >= 6 and len(word) <= 9) else 'no')