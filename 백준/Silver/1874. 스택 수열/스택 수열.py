N = int(input())

stack = []
stack_result = []
lst = []
result = []

for i in range(N):
    lst.append(int(input()))

num = 1
idx = 0

while num <= N:
    if stack and stack[-1] == lst[idx]:
        stack_result.append(stack.pop())
        idx += 1
        result.append('-')
    else:
        stack.append(num)
        num += 1
        result.append('+')

for j in range(len(stack)):
    stack_result.append(stack.pop())
    result.append('-')

if stack_result == lst:
    for k in result:
        print(k)
else:
    print('NO')