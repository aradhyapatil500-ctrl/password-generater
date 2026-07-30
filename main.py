import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

print("=" * 35)
print("      PASSWORD GENERATOR")
print("=" * 35)

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Please enter a number greater than 0.")
    else:
        password = generate_password(length)
        print("\nGenerated Password:")
        print(password)

except ValueError:
    print("Please enter a valid number.")
