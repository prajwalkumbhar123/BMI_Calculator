# BMI Calculator in Python

def calculate_bmi(weight, height):
    return weight / (height ** 2)

print("=== BMI Calculator ===")

try:
    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in meters): "))

    if weight <= 0 or height <= 0:
        print("Weight and height must be positive numbers.")
    else:
        bmi = calculate_bmi(weight, height)
        print(f"\nYour BMI is: {bmi:.2f}")

        if bmi < 18.5:
            print("Category: Underweight")
        elif bmi < 24.9:
            print("Category: Normal weight")
        elif bmi < 29.9:
            print("Category: Overweight")
        else:
            print("Category: Obese")

except ValueError:
    print("Please enter valid numeric values.")
