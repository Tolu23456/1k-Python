"""
Discount Checker: Apply discount if price > 100.
   - Hint: if price > 100.
   - Components: original, final.
"""

price = int(input("Enter total price: "))

if price > 100:
    price *= 0.9
    print(f"Discount applied! Your final price is {price}")
else:
    print(f"No discount applied! Price is {price}")