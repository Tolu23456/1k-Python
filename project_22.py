# ---

# **Project 22 – List Average**
# **Topic:** List

# **Task:**
# Calculate the average of numbers in a list.

# **Hints:**

# * Use `sum()` and `len()`

# **Example expected output:**

# ```
# List: [2,4,6]
# Average: 4.0
# ```

# ---

lst = [2, 4, 6]

sum_of_list = 0
length_of_list = 0
avg = 0

for item in lst:
    length_of_list += 1
    sum_of_list += item

avg = sum_of_list / length_of_list

print(f"List: {lst} \nAverage: {avg}")
