"""
Triangle Valid: Check if 3 sides can form a triangle.
   - Hint: Sum of any 2 sides must be > 3rd side.
   - Components: a, b, c.
"""

a = int(input("Side A: "))
b = int(input("Side B: "))
c = int(input("Side C: "))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print("Valid Triangle.")
else:
    print("Invalid Triangle.")