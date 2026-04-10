# ---

# **Project 26 – Swap Two Numbers**
# **Topic:** Variables

# **Task:**
# Swap two numbers without using a third variable.

# **Hints:**

# * Use `a, b = b, a`

# **Example expected output:**

# ```
# Before swap: a=5, b=10
# After swap: a=10, b=5
# ```

# ---

a = 5
b = 10

print(f"Before: a = {a}, b = {b}")

a, b = b, a

print(f"After: a = {a}, b = {b}")