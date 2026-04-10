"""
Leap Year: Determine if a year is a leap year.
   - Hint: Use n % 4 == 0 logic.
   - Components: year.
"""
try:
    year = int(input("Enter year: "))
    
    if year % 4 == 0:
        print(f"{year} is a leap year.")
    else:
        print(f"{year} is not a leap year.")
except ValueError as e:
    print(e)