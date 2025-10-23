import string
import random

letters = string.ascii_letters
digits = string.digits
special_characters = string.punctuation
all_characters = letters + digits + special_characters
password_length = int(input("Enter the desired password length: "))

for i in range(password_length):
    password = ''.join(random.sample(all_characters, password_length))
    
print("Generated password:", password)
