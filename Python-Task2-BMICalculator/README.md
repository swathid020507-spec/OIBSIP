# BMI Calculator

## Oasis Infobyte Python Programming Internship

### Task 2 - BMI Calculator

## Project Description

This project is a simple command-line BMI (Body Mass Index) Calculator developed using Python.

The program asks the user to enter their weight in kilograms and height in metres. It then calculates the BMI and classifies the result into standard BMI categories.

## Features

- Accepts weight in kilograms (kg)
- Accepts height in metres (m)
- Calculates BMI using the formula:
  
  BMI = weight / (height²)

- Displays the BMI value rounded to 2 decimal places
- Displays the BMI category
- Validates user input
- Rejects non-numeric input
- Rejects negative values
- Displays a helpful error message for invalid input

## BMI Categories

| BMI Range | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5 - 24.9 | Normal weight |
| 25 - 29.9 | Overweight |
| 30 and above | Obese |

## Technologies Used

- Python
- input()
- Basic arithmetic

## How to Run

1. Make sure Python is installed on your computer.
2. Open the project folder in Visual Studio Code.
3. Open `main.py`.
4. Open the terminal in Visual Studio Code.
5. Run the following command:

```bash
python main.py

6. Enter your weight in kilograms.
7. Enter your height in metres.
8. The program will display your BMI and BMI category.

## Example Output

```text
===== BMI CALCULATOR =====

Enter your weight in kilograms (kg): 60
Enter your height in metres (m): 1.65

Your BMI is: 22.04
Category: Normal weight

Project Structure

Python-Task2-BMICalculator/
│
├── main.py
├── README.md
│
└── screenshots/
    ├── bmi_output.png
    └── validation.png

Internship

This project was developed as part of the Oasis Infobyte Python Programming Internship.

Task: Task 2 - BMI Calculator
Track: Python Programming