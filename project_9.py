# ---

# **Project 9 – Max in Tuple**
# **Topic:** Tuples

# **Task:**
# Create a tuple of numbers and print the largest value.

# **Hints:**

# * Use `max()` function.
# * Tuples are immutable.

# **Example expected output:**

# ```
# Numbers: (4, 7, 1, 9)
# Maximum: 9
# ```

# ---

num = (4, 7, 1, 9)
maximum = 0

for i in num:
    if i > maximum:
        maximum = i

print(maximum)