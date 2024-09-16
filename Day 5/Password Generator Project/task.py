import random
from traceback import print_tb

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Easy Level
# password = ""
# password2 = ""
# for letter_pass in range(0,nr_letters):
#     password += random.choice(letters)
#
# for numbers_num in range(0, nr_numbers):
#      password += random.choice(numbers)
#
# for symbols_pass in range(0,nr_symbols):
#     password += random.choice(symbols)
#
# for passw_ in range(0, len(password)):
#     password2 += random.choice(password)
#
# print(end="".join(password2))

#Hard Level
password_list = []
for letter_pass in range(0,nr_letters):
    password_list += random.choice(letters)

for numbers_num in range(0, nr_numbers):
     password_list += random.choice(numbers)

for symbols_pass in range(0,nr_symbols):
    password_list += random.choice(symbols)

print(password_list)
random.shuffle(password_list)
print(password_list)

password3 = ""
for char in password_list:
    password3 += char

print(f"You password is: {password3}")