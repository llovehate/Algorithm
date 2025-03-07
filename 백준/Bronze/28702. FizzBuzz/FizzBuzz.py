N1 = input()
N2 = input()
N3 = input()

num = 0

if N1 == "Fizz" or N1 == "Buzz" or N1 == "FizzBuzz":
    pass
else:
    num = int(N1) + 3

if N2 == "Fizz" or N2 == "Buzz" or N2 == "FizzBuzz":
    pass
else:
    num = int(N2) + 2

if N3 == "Fizz" or N3 == "Buzz" or N3 == "FizzBuzz":
    pass
else:
    num = int(N3) + 1

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)