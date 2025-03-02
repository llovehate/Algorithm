import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
cards = list(sys.stdin.readline().split())
M = int(sys.stdin.readline().strip())
target_cards = list(sys.stdin.readline().split())

cards_cnt = Counter(cards)

for num in target_cards:
    print(cards_cnt[num], end=" ")