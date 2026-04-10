"""
Prime Checker: Verify if a number is prime.
   - Hint: Check for factors from 2 to square root of n.
   - Components: flag, break.
   
"""

check = int(input("Enter number: "))

for i in range(2, check):
    if check % i == 0:
        print(f"{check} is not a Prime Number")
        break
else:
    print(f"{check} is a Prime Number")
