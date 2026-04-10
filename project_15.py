# ---

# **Project 15 – Factorial Using Function**
# **Topic:** Functions

# **Task:**
# Create a function that returns factorial of a number.

# **Hints:**

# * Use `for` loop or recursion.

# **Example expected output:**

# ```
# Enter number: 5
# Factorial: 120
# ```

# ---

factorial = int(input("Enter number: "))
factorial_sum = 1


for n in range(factorial, 0, -1):
    factorial_sum *= n

print(f"Factorial: {factorial_sum}")