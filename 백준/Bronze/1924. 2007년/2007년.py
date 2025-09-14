day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
x, y = map(int, input().split())
num = 0
days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

if x >= 2:
    for i in range(x-1):
        num += day[i]
num += y

print(days[num % 7])