import random
import string

length=int(input("Enter the password length:  "))

def generate_password(length, use_digits, use_special):
    letters = string.ascii_letters
    digits = string.digits if use_digits else ""
    special = string.punctuation if use_special else ""
    all_chars = letters + digits + special

    print(digits)
    print (all_chars)

generate_password(12, True, False)



