# **Project 1 – Simple Calculator**
# **Topic:** Variables

# **Task:**
# Create a program that takes two numbers and prints their sum, difference, product, and division.

# **Hints:**

# * Use variables to store user input.
# * Convert input to `int` or `float`.

# **Example expected output:**

# ```
# Enter first number: 10
# Enter second number: 5
# Sum: 15
# Difference: 5
# Product: 50
# Division: 2.0
# ```

try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    if second_number != 0:
        division = first_number / second_number
        difference = first_number - second_number
        product = first_number * second_number
        sum = first_number + second_number

        print(f"Sum: {sum}")
        print(f"Difference: {difference}")
        print(f"Product: {product}")
        print(f"Division: {division}")
    else:
        print("\nCannot divide by zero")
        difference = first_number - second_number
        product = first_number * second_number
        sum = first_number + second_number

        print(f"Sum: {sum}")
        print(f"Difference: {difference}")
        print(f"Product: {product}")
    

except ValueError:
    print("\nInput can only be integers")


