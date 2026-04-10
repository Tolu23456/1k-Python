# ---

# **Project 5 – Type Conversion**
# **Topic:** Type Casting

# **Task:**
# Ask the user for a number as a string, convert it to integer, then float, and print both.

# **Hints:**

# * Use `int()` and `float()` functions.

# **Example expected output:**

# ```
# Enter a number: 12
# Integer: 12
# Float: 12.0
# ```

# ---

str_num = input("Enter a number: ")

print(f"Integer: {int(str_num)}")
print(f"Float: {float(str_num)}")