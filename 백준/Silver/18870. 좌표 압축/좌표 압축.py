N = int(input())
lst = list(map(int, input().split()))
num_set = sorted(set(lst))

rank = {num: idx for idx, num in enumerate(num_set)}

result = [rank[num] for num in lst]

print(*result)