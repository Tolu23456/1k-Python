"""
Range Guard: Check if value is between 10 and 50.
   - Hint: Use "and" keyword.
   - Components: val.
"""

val = int(input("Enter number: "))

if 10 <= val <= 50:
    print("Value is within the safe zone.")
else:
    print("Value is outside the range.")