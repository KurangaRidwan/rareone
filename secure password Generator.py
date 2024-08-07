import random
import string

def generate_secure_password(length=12):
    if length < 12:
        raise ValueError("Password length should be at least 12 characters")

    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password has at least one character from each set
    all_characters = lower + upper + digits + symbols
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to avoid predictable patterns
    random.shuffle(password)

    # Convert list to string and return
    return ''.join(password)

length = int(input("Enter the desired password length (minimum 12 characters): "))
print("Generated secure password:", generate_secure_password(length))
