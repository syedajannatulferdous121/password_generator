import random
import string

def generate_password(desired_password, length=12, include_digits=True, include_special_chars=True):
    extra_characters = ""
    if include_digits:
        extra_characters += string.digits
    if include_special_chars:
        extra_characters += string.punctuation

    password_length = max(length, len(desired_password) + 4)  # Minimum length of 12 characters
    missing_characters = password_length - len(desired_password)
    
    if missing_characters <= 0:
        return desired_password
    
    extra_chars = random.sample(extra_characters, missing_characters)
    password = desired_password + ''.join(extra_chars)
    password = ''.join(random.sample(password, len(password)))  # Shuffle the password
    
    return password

desired_password = input("Enter your desired password: ")
desired_length = int(input("Enter desired password length: "))
include_digits = input("Include digits? (Y/N): ").upper() == "Y"
include_special_chars = input("Include special characters? (Y/N): ").upper() == "Y"

generated_password = generate_password(desired_password, desired_length, include_digits, include_special_chars)

print("Generated Password:", generated_password)
