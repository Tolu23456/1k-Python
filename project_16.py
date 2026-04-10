# ---

# **Project 16 – Reverse a List**
# **Topic:** List

# **Task:**
# Reverse a given list without using built-in `reverse()` function.

# **Hints:**

# * Use slicing `list[::-1]` or a loop.

# **Example expected output:**

# ```
# Original: [1,2,3,4]
# Reversed: [4,3,2,1]
# ```

# ---

original_list = [1, 2, 3, 4, 5]
reversed_list = []

for n in original_list:
    reversed_list.insert(0, n)

print(f"Original: {original_list}")
print(f"Revesered: {reversed_list}")