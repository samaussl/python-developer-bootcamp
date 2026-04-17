# Utilizes iterative loops and character randomization.

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


pass_letters = ""
pass_symbols = ""
pass_numbers = ""
new_password = ""

for no_letters in range(0, nr_letters):
    random_char = random.choice(letters)
    pass_letters += random_char
# print(pass_letters)

for no_symbols in range(0, nr_symbols):
    random_symb = random.choice(symbols)
    pass_symbols += random_symb
# print(pass_symbols)

for no_numbers in range(0, nr_numbers ):
    random_numb = random.choice(numbers)
    pass_numbers += random_numb
# print(pass_numbers)

print(pass_letters + pass_symbols + pass_numbers)

# Hard Way : shuffling the all characters not in an order
password = [pass_letters, pass_symbols, pass_numbers]
shuffled_password = random.sample(password, len(password))


for pass_char in range(0, len(shuffled_password)):
    new_password += shuffled_password[pass_char]

print(new_password)
