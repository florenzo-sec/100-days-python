from string import ascii_letters, digits,punctuation
from random import choice,shuffle

print("Welcome to the PyPassword Generator!")

letters = int(input("How many letters would you like? "))
symbols = int(input("How many symbols would you like? "))
numbers = int(input("How many numbers would you like? "))

password = []

for i in range(letters):
    password += choice(ascii_letters)
for i in range(symbols):
    password += choice(punctuation)
for i in range(numbers):
    password += choice(digits)

shuffle(password) #randomize the pattern

print(f"Here's your password:\n{''.join(char for char in password)}")



