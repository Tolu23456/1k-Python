"""
Legal Driver: Check if age is 18+.
   - Hint: Use >= operator.
   - Components: age.

"""

try:
    age = int(input("Enter age: "))
    
    if age >= 18:
        print("You are old enough to drive.")
    else:
        print("You must be 18 to drive.")
except ValueError as e:
    print(e)