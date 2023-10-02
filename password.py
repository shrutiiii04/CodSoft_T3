import random
import string

def password(length):
    words = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(words) for _ in range(length))
    return password

try:
    p_length = int(input("Enter the desired length of the password: "))
    if p_length <= 0:
        print("Length of password must be greater than 0.")
    else:
        password = password(p_length)
        print("Generated Password:", password)
except ValueError:
    print("Invalid input!!")
