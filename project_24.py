# ---

# **Project 24 – Input Validation**
# **Topic:** Exception

# **Task:**
# Ask user to enter an integer. Handle if they enter non-integer.

# **Hints:**

# * Use `try-except` with `ValueError`

# **Example expected output:**

# ```
# Enter number: abc
# Invalid input!
# ```

# ---

try:
    n = int(input("Enter number: "))
except ValueError:
    print("Invalid Input!")