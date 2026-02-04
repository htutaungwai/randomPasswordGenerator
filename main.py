import random
import string

def get_yn_option(option):
    if option in ("n", "N", "no", "No", "NO"):
        return  False
    else:
        return  True

password_digit = get_yn_option(input("y/n? Would you use digit numbers in the password.The default answer is yes. \n"))
password_special = get_yn_option(input("y/n? Would you use digit numbers in the password. The default answer is yes. \n"))

while True:
    try:
        password_length = int(input("Enter the password length:  "))
        if 0 < password_length < 100:  break
        else:
            print("Input must be between 0 and 100.")
    except ValueError:
        print("Invalid input! Please enter a whole number")

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

    password = ''.join(str(x) for x in password)
    print(password)

generate_password(password_length, password_digit, password_special)



