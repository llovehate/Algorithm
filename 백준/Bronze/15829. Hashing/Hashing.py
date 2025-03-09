N = int(input())
my_str = input()

r = 31
M = 1234567891

result = 0
power = 1

for i in range(N):
    str_v = ord(my_str[i]) - ord('a') + 1
    result = (result + str_v * power) % M
    power = (power * r) % M

print(result)