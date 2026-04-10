# ---

# **Project 18 – Sum of Even Numbers**
# **Topic:** Loops

# **Task:**
# Find the sum of all even numbers in a list.

# **Hints:**

# * Iterate over list and add if number % 2 == 0

# **Example expected output:**

# ```
# List: [1,2,3,4,5]
# Sum of evens: 6
# ```

# ---

n_list = [1,2,3,4,5]
sum_of_even = 0

for n in n_list:
    if n % 2 == 0:
        sum_of_even += n

print(f"List: {n_list}")
print(f"Sum of evens: {sum_of_even}")