# ---

# **Project 4 – Sum of Numbers Using Loop**
# **Topic:** Loops

# **Task:**
# Calculate the sum of all numbers from 1 to `n` using a `for` loop.

# **Hints:**

# * Use `range(1, n+1)`.
# * Keep adding numbers to a total variable.

# **Example expected output:**

# ```
# Enter n: 5
# Sum: 15
# ```

# ---

n = int(input("Enter n: "))
sum = 0

for i in range(1, n+1):
    sum += i

print(f"Sum: {sum}")