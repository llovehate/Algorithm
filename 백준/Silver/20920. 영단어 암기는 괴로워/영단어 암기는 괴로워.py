import sys
from collections import Counter
input = sys.stdin.readline

N, M = map(int, input().split())
lst = []

for i in range(N):
    word = input().strip()
    if len(word) >= M:
        lst.append(word)

word_cnt = Counter(lst)
sorted_words = sorted(word_cnt.items(), key=lambda item: (-item[1], -len(item[0]), item[0]))

for i in sorted_words:
    print(i[0])