def dfs(n, num, add, sub, mul, div):
    global min_v, max_v
    if n == N:
        min_v = min(min_v, num)
        max_v = max(max_v, num)
        return
 
    if add:
        dfs(n+1, num+lst[n], add-1, sub, mul, div)
    if sub:
        dfs(n+1, num-lst[n], add, sub-1, mul, div)
    if mul:
        dfs(n+1, num*lst[n], add, sub, mul-1, div)
    if div:
        dfs(n+1, int(num/lst[n]), add, sub, mul, div-1)
 
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    add, sub, mul, div = map(int, input().split())
    lst = list(map(int, input().split()))
    min_v = int(1e9)
    max_v = int(-1e9)
    dfs(1, lst[0], add, sub, mul, div)
 
    print(f'#{tc} {max_v-min_v}')