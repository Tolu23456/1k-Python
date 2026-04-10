"""
Max of Two: Identify the larger of two numbers.
   - Hint: Use if/else.
   - Components: num1, num2.

"""
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1 < num2:
        print(f"{num1} is less than {num2}")
    else:
        print("The numbers are equal")
except ValueError as e:
    print(e)