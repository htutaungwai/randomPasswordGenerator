import random
import string
player_length=int(input("Enter the password length:  "))

def generate_password(length, use_digits, use_special):
    letters = string.ascii_letters
    digits = string.digits if use_digits else ""
    special = string.punctuation if use_special else ""
    password = []


    for x in range (length):
        pool = []
        if letters:
            pool.append(random.choice(letters))
        if use_digits and digits:
            pool.append(random.choice(digits))
        if use_special and special:
            pool.append(random.choice(special))

        if pool:
            password.append(random.choice(pool))



        print(password)



generate_password(6, True, True)



