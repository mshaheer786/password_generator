import random
import string

def generate_password(length):
    if length < 4:
        return "Password should be greater than 4 character !"
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_charcter= lowercase+uppercase+digits+symbols
    
    password=""
    password += random.choice(lowercase)
    password += random.choice(uppercase)
    password += random.choice(digits)
    password += random.choice(symbols)
    
    for i in range(length -4):
        password+=random.choice(all_charcter)
        pass_list=list(password)
        random.shuffle(pass_list)
        password="".join(pass_list)
        return password
    
try:
    length = int(input("Enter the length of the password (minimum 4): "))
    password = generate_password(length)
    print(f"Generated password is: {password}")
except ValueError:
    print("Invalid input. Please enter a number.")
