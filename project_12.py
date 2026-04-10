# ---

# **Project 12 – Temperature Converter**
# **Topic:** Variables

# **Task:**
# Convert Celsius to Fahrenheit and vice versa.

# **Hints:**

# * Use the formula F = (C * 9/5) + 32

# **Example expected output:**

# ```
# Enter temperature in Celsius: 25
# Temperature in Fahrenheit: 77.0
# ```

# ---

C = int(input("Enter temperature in Celsius: "))

F = (C * 9/5) + 32

print(f"Temperature in Fahrenheit: {F}")