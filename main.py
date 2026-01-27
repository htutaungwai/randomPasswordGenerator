import random
import string
player_length=int(input("Enter the password length:  "))

def generate_password(length, use_digits, use_special):
    letters = string.ascii_letters
    digits = string.digits if use_digits else ""
    special = string.punctuation if use_special else ""
    # all_chars = letters + digits + special

    password_chars = []

    if letters:
        password_chars.append(random.choice(letters))
    if use_digits and digits:
        password_chars.append(random.choice(digits))
    if use_special and special:
        password_chars.append(random.choice(special))
    print(password_chars)

generate_password(12, True, True)



