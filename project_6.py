# ---

# **Project 6 – Divide Safely**
# **Topic:** Exception

# **Task:**
# Ask the user for two numbers and divide them. Handle division by zero.

# **Hints:**

# * Use `try-except` block.
# * Catch `ZeroDivisionError`.

# **Example expected output:**

# ```
# Enter first number: 10
# Enter second number: 0
# Cannot divide by zero!
# ```

# ---


try:
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    print(f"Division: {first_number/second_number}")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Only numbers are allowed!")