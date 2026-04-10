"""
BMI Category: Categorize BMI results.
    - Hint: Use multiple elif ranges.
    - Components: height, weight.
"""

bmi = int(input("Enter BMI: "))

if 1 <= bmi <= 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Healthy weight")
elif 25.0 <= bmi <= 29.9:
    print("Overweight")
elif 30.0 <= bmi <= 10000:
    print("Obese")
else:
    print("Invalid BMI")