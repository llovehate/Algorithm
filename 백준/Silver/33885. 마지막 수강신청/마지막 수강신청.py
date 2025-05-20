N, M = map(int, input().split())

subjects = []
possibility = False

for _ in range(N):
    parts = input().split()
    c = int(parts[0])
    s = int(parts[1])
    times = set()
    for i in range(s):
        day = parts[2 + i * 2]
        hour = int(parts[3 + i * 2])
        times.add((day, hour))
    subjects.append((c, times))


def backtrack(idx, c_sum, times):
    global possibility
    if c_sum >= M:
        possibility = True
        return
    if idx == N or possibility:
        return

    c, t_set = subjects[idx]

    # 과목 선택하는 경우
    # 현재까지의 시간표와 후보 시간표가 겹치는지 검증
    if not (t_set & times):
        backtrack(idx + 1, c_sum + c, times | t_set)

    # 과목 선택하지 않는 경우
    backtrack(idx + 1, c_sum, times)

backtrack(0, 0, set())

print('YES' if possibility else 'NO')