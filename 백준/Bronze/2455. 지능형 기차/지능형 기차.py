max_people = 0
now_people = 0

for _ in range(4):
    leave, ride = map(int, input().split())
    now_people -= leave
    now_people += ride
    max_people = max(max_people, now_people)

print(max_people)