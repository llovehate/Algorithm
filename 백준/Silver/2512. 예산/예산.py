N = int(input())
lst = list(map(int, input().split()))
M = int(input())

if sum(lst) <= M:
    print(max(lst))
else:
    start = 0
    end = max(lst)
    result = 0

    while start <= end:
        mid = (start + end) // 2
        new_lst = []
        for i in lst:
            if i <= mid:
                new_lst.append(i)
            else:
                new_lst.append(mid)

        if sum(new_lst) <= M:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    print(result)