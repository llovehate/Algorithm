A, B, C = map(int, input().split())
result = 0
arrive_car = []
departure_car = []

for _ in range(3):
    arrive, departure = map(int, input().split())
    arrive_car.append(arrive)
    departure_car.append(departure)

arrive_car.sort()
departure_car.sort()
time = arrive_car[0]
parking_lot = 1

while time < departure_car[2]:
    if parking_lot == 1:
        result += A
    elif parking_lot == 2:
        result += (2 * B)
    elif parking_lot == 3:
        result += (3 * C)

    time += 1
    if time in arrive_car:
        parking_lot += arrive_car.count(time)
    if time in departure_car:
        parking_lot -= departure_car.count(time)

print(result)