# range function using for loop
# for number in range(1, 11, 3):
#     print(number)

# total = 0
# for number in range(1 ,101):
#     total += number
# print(total)

for number in range(1, 101):

    if (number % 3 == 0) and (number % 5 == 0):
        print("FizzBuzz")
        continue

    if number % 3 == 0:
        print("Fizz")
        continue

    if number % 5 == 0:
        print("Buzz")
        continue

    print(number)