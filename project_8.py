# ---

# **Project 8 – Sum List Elements**
# **Topic:** List

# **Task:**
# Create a list of numbers and print the sum of its elements.

# **Hints:**

# * Use `sum()` function or a loop.

# **Example expected output:**

# ```
# Numbers: [1, 2, 3, 4, 5]
# Sum: 15
# ```

# ---

num = [1, 2, 3, 4, 5]
sum = 0

for n in num:
    sum += n

print("Sum:", sum)