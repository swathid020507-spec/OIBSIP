import random
import string

print("=" * 40)
print("     RANDOM PASSWORD GENERATOR")
print("=" * 40)

while True:
    try:
        length = int(input("\nEnter password length (minimum 8): "))

        if length < 8:
            print("Error: Password length must be at least 8.")
            continue

        print("\nChoose character types:")
        print("1. Lowercase letters")
        print("2. Uppercase letters")
        print("3. Numbers")
        print("4. Special characters")

        choices = input(
            "Enter choices separated by commas (e.g., 1,2,3,4): "
        )

        selected = set(choices.replace(" ", "").split(","))

        if not selected or not selected.issubset({"1", "2", "3", "4"}):
            print("Error: Please select valid options (1-4).")
            continue

        characters = ""
        required = []

        if "1" in selected:
            characters += string.ascii_lowercase
            required.append(random.choice(string.ascii_lowercase))

        if "2" in selected:
            characters += string.ascii_uppercase
            required.append(random.choice(string.ascii_uppercase))

        if "3" in selected:
            characters += string.digits
            required.append(random.choice(string.digits))

        if "4" in selected:
            characters += string.punctuation
            required.append(random.choice(string.punctuation))

        if length < len(required):
            print("Error: Length is too short for your selected types.")
            continue

        remaining = [
            random.choice(characters)
            for _ in range(length - len(required))
        ]

        password_chars = required + remaining
        random.shuffle(password_chars)
        password = "".join(password_chars)

        print("\nGenerated password:", password)

        again = input("\nGenerate another password? (yes/no): ")
        if again.strip().lower() != "yes":
            print("Thank you for using the Password Generator!")
            break

    except ValueError:
        print("Error: Please enter a whole number for the length.")