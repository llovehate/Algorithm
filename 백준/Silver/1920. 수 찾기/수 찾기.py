N = int(input())
N_lst = list(map(int, input().split()))
N_lst = set(N_lst)
M = int(input())
M_lst = list(map(int, input().split()))

for i in M_lst:
    N_len = len(N_lst)
    N_lst.add(i)
    if N_len == len(N_lst):
        print(1)
    else:
        N_lst.discard(i)
        print(0)