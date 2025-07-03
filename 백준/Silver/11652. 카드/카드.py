import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
lst = []
candidates = []

for _ in range(N):
    card = int(input())
    lst.append(card)

card_cnt = Counter(lst)
max_freq = max(card_cnt.values())

for num, cnt in card_cnt.items():
    if cnt == max_freq:
        candidates.append(num)

print(min(candidates))