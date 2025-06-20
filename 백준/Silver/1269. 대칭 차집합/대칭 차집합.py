num_A, num_B = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
result = set()

B_min = B - A
A_min = A - B

for i in B_min:
    result.add(i)
for j in A_min:
    result.add(j)

print(len(result))