import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
password_letters = int(input("How many letters would you like in your password?\n"))
password_symbols = int(input(f"How many symbols would you like?\n"))
password_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for i in range(password_letters):
    password += random.choice(letters)

for i in range(password_symbols):
    password += random.choice(symbols)

for i in range(password_numbers):
    password += random.choice(numbers)
print("Your password is :",password)


# Hard Password
password_list = []
random.shuffle(password_list)

for i in range(password_letters):
    password_list.append(random.choice(letters))

for i in range(password_symbols):
    password_list.append(random.choice(symbols))

for i in range(password_numbers):
    password_list.append(random.choice(numbers))
# hard_password is now in a list so we need to convert it into string. we gonna use for loops for that
hard_password = ""
for char in password_list:
    hard_password += random.choice(password_list)
print("Your hard Password:",hard_password)
