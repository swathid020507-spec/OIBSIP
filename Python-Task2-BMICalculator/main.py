# BMI Calculator
# Oasis Infobyte Python Programming Internship - Task 2

print("===== BMI CALCULATOR =====")

while True:
    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in metres (m): "))

        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be greater than zero.")
            print("Please try again.\n")
            continue

        bmi = weight / (height ** 2)

        print(f"\nYour BMI is: {bmi:.2f}")

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"

        print(f"Category: {category}")

        break

    except ValueError:
        print("Error: Please enter numbers only.")
        print("Please try again.\n")